#!/bin/bash


function sanitize_str() {
    input_str=$1

    # Pipe through xargs to strip outer whitespace, then trim it and convert to lower case
    echo "$input_str" | xargs | tr '[:upper:]' '[:lower:]'
}


function topology() {
    GRAPH_DIRECTION=$1
    ENVIRONMENT=${2:-"develop"}
    
    SUPPORTED_DIRECTIONS=("horizontal" "vertical")
    SUPPORTED_ENVS=("dev" "develop" "development" "desenvolvimento" "prod" "production" "producao")
    
    COMPOSE_YAML_BASENAME="docker-compose"

    case $ENVIRONMENT in
        dev|develop|development|desenvolvimento)
            ENV_FOLDER="develop"
            DOCKER_COMPOSE_FILE=$COMPOSE_YAML_BASENAME.yml;;
        prod|production|producao)
            ENV_FOLDER="production"
            DOCKER_COMPOSE_FILE=$COMPOSE_YAML_BASENAME.yml;;
        *)
            echo -n "Environment '$ENVIRONMENT' not supported. Choices are: "
            printf "%s," "${SUPPORTED_ENVS[@]}" | sed 's/,$//'
            echo
            exit 1;;
    esac

    DOCKER_COMPOSE_DIAGRAM_LOCATION="resources/docs/images"

    echo "Generating topology diagram for '$ENVIRONMENT' environment..."

    OUTPUT_FILE="docker-topology-$ENV_FOLDER.png"
    DOCKER_COMPOSE_FILE_PATH="infra/docker/$ENV_FOLDER/$DOCKER_COMPOSE_FILE"

    chmod 777 "./$DOCKER_COMPOSE_DIAGRAM_LOCATION"

    echo "Docker Compose YAML to be used:   $DOCKER_COMPOSE_FILE_PATH"
    echo "Topology diagram PNG saved in:    $DOCKER_COMPOSE_DIAGRAM_LOCATION/$OUTPUT_FILE"

    SANITIZED_DIRECTION=$(sanitize_str $GRAPH_DIRECTION)

    DOCKERCMD=(
        docker run \
            -u $(id -u):$(id -g) \
            --rm \
            -it \
            --name dcv \
            -v "$(pwd):/input:rw" \
            -v "$(pwd)/$DOCKER_COMPOSE_DIAGRAM_LOCATION:/output:rw" \
            pmsipilot/docker-compose-viz \
            render \
                -m \
                image \
                --force \
                --output-file /output/$OUTPUT_FILE \
                $DOCKER_COMPOSE_FILE_PATH
    )

    case $SANITIZED_DIRECTION in
        horizontal)
            echo "Graph direction:                  $SANITIZED_DIRECTION";;
        vertical)
            echo "Graph direction:                  $SANITIZED_DIRECTION"
            DOCKERCMD+=( --horizontal );;
        *)
            echo -n "Graph direction '$SANITIZED_DIRECTION' not supported. Choices are: "
            printf "%s," "${SUPPORTED_DIRECTIONS[@]}" | sed 's/,$//'
            echo
            exit 1;;
    esac

    # Safely executes Docker command
    "${DOCKERCMD[@]}"
}

$@
