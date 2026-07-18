#!/bin/bash

function main() {
    prune
    check
}

function prune() {
    CONTAINER_LIST=$(docker container ls -aq)

    if [[ -n $CONTAINER_LIST ]] then
        echo "Stopping and removing containers..."

        docker container stop $CONTAINER_LIST
        docker container rm $CONTAINER_LIST
        docker container prune --force
    fi

    IMAGE_LIST=$(docker image ls -aq)

    if [[ -n $IMAGE_LIST ]] then
        echo "Removing images..."

        docker image rm $IMAGE_LIST
        docker image prune --force
    fi

    VOLUME_LIST=$(docker volume ls -q)

    if [[ -n $VOLUME_LIST ]] then
        echo "Removing volumes..."

        docker volume rm $VOLUME_LIST
        docker volume prune --force
    fi

    echo "Removing unused networks..."
	docker network prune --force
}

function check() {
	docker container ls -a
	docker image ls -a
	docker volume ls
	docker network ls
}

main "$@"
