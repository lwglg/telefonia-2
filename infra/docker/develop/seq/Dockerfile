FROM datalust/seq:latest
  
# Ingestion/API + clients (HTTP, or HTTPS if TLS is configured)
EXPOSE 80

# Ingestion over raw TCP (GELF/syslog not included; this is the
# structured HTTP ingestion endpoint used by most clients)
EXPOSE 5341
 
HEALTHCHECK \
    --interval=30s \
    --timeout=10s \
    --retries=5 \
    CMD curl -f http://localhost/health || exit 1
