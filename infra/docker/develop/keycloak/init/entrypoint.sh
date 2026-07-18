#!/bin/bash

set -e

# Tell the system to look in our custom directory for psql's libraries
export LD_LIBRARY_PATH="/opt/keycloak/psql-libs:$LD_LIBRARY_PATH"

echo "Starting Keycloak..."

# Always use exec so Keycloak safely catches shutdown signals
exec /opt/keycloak/bin/kc.sh --verbose "$@"
