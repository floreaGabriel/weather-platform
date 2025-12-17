# Stage 1: Builder
FROM python:3.11-slim AS builder

WORKDIR /build

# copy only what's needed for install
COPY pyproject.toml .
COPY src/ src/

# create venv and install
RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install .


# Stage 2: Runtime
FROM python:3.11-slim

# create non-root user
RUN addgroup --system app && adduser --system --ingroup app app

# copy venv from builder
COPY --from=builder /venv /venv

# copy application code
WORKDIR /app
COPY --chown=app:app src/ src/

# healthcheck using python (no curl in slim image)
HEALTHCHECK --interval=30s --timeout=3s \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

USER app

# run with uvicorn
CMD ["/venv/bin/uvicorn", "src.prediction_api.main:app", "--host", "0.0.0.0", "--port", "8000"]