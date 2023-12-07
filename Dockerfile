FROM python:3.11

WORKDIR /app
COPY pyproject.toml poetry.lock ./

# configure Poetry
ENV POETRY_VERSION=1.6.1

# installing Poetry
RUN pip install poetry==${POETRY_VERSION} && poetry install --no-root --no-directory
COPY src/ ./src/
RUN poetry install --only main
RUN poetry run opentelemetry-bootstrap --action=install

# run the application
CMD ["poetry", "run", "opentelemetry-instrument", "celery", "-A", "src.tasks.app", "worker", "-l", "INFO"]
