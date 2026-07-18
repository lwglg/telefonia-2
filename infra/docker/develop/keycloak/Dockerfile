# Stage 1: Build stage to download the DB client
FROM redhat/ubi9-minimal AS builder

RUN microdnf install -y postgresql && microdnf clean all

# Create a clean directory and copy dependencies, explicitly EXCLUDING core system libraries
RUN mkdir -p /opt/psql-libs && \
    cp $(ldd /usr/bin/psql | grep "=> /" | awk '{print $3}' | grep -vE 'libc\.so|libm\.so|libdl\.so|libpthread\.so|ld-linux') /opt/psql-libs/

# Stage 2: Final hardened Keycloak image
FROM quay.io/keycloak/keycloak:latest

ENV KC_DB=postgres \
    KC_PROXY_HEADERS=xforwarded \
    KC_HTTP_ENABLED=true \
    KC_HOSTNAME_STRICT=false \
    KC_HEALTH_ENABLED=true \
    KC_METRICS_ENABLED=true

COPY --from=builder /usr/bin/psql /usr/bin/psql
COPY --from=builder /opt/psql-libs/ /opt/keycloak/psql-libs/

ENV INFRA_ROOT=./infra/docker/develop/keycloak

COPY ${INFRA_ROOT}/init/create_kc_admin_user.sql /opt/keycloak/create_kc_admin_user.sql
COPY ${INFRA_ROOT}/init/create_kc_admin_user.sh /opt/keycloak/bin/create_kc_admin_user.sh 
COPY ${INFRA_ROOT}/init/entrypoint.sh /opt/keycloak/bin/entrypoint.sh

USER root
RUN chmod +x /opt/keycloak/bin/entrypoint.sh
RUN chmod +x /opt/keycloak/bin/create_kc_admin_user.sh

USER 1000

# Optional: Pre-build the Keycloak configuration for faster startup
RUN /opt/keycloak/bin/kc.sh build \
    --health-enabled=true \
    --metrics-enabled=true

EXPOSE 8080

# Healthcheck - Keycloak exposes /health/ready and /health/live
HEALTHCHECK --interval=30s \
    --timeout=10s \
    --start-period=40s \
    --retries=5 \
    CMD curl -f http://localhost:8080/health/ready || exit 1

ENTRYPOINT ["/opt/keycloak/bin/entrypoint.sh"]
