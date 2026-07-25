FROM rabbitmq:3-management 
 
RUN rabbitmq-plugins enable --offline rabbitmq_management

# AMQP (client connections)
EXPOSE 5672

# AMQP over TLS
EXPOSE 5671

# Management HTTP API / Web UI
EXPOSE 15672
 
HEALTHCHECK \
    --interval=30s \
    --timeout=10s \
    --retries=5 \

CMD ["rabbitmq-diagnostics", "-q", "ping"]
