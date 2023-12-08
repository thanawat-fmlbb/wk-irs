# How to run

To run this,
```sh
poetry shell  # activates the shell first
OTEL_RESOURCE_ATTRIBUTES=service.name=sp4-irs \
OTEL_EXPORTER_OTLP_ENDPOINT="http://localhost:4317" \
OTEL_EXPORTER_OTLP_PROTOCOL=grpc \
opentelemetry-instrument celery -A src.tasks.app worker -l INFO
```
