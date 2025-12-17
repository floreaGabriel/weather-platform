from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Response model for health check endpoint."""

    status: str


class ReadyResponse(BaseModel):
    """Response model for ready check endpoint."""

    status: str
