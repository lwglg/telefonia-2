#!/bin/bash

set -e

echo "Creating system admin credentials..."

# Example using PostgreSQL client (adjust credentials/host as needed)
PGPASSWORD="$KC_DB_PASSWORD" psql \
    -v ON_ERROR_STOP=1 \
    -h "$KC_DB_HOSTNAME" \
    -U "$KC_DB_USERNAME" \
    -d "$KC_DB_NAME" \
    -p "$KC_DB_PORT" \
    -f /opt/keycloak/create_kc_admin_user.sql

exit 0
