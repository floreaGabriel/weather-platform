from fastapi import APIRouter

from src.prediction_api.models.schemas import HealthResponse, ReadyResponse

router = APIRouter(tags=["Health"])


@router.get("/health", response_model=HealthResponse)
def health_check():
    """Check if the service is running."""
    return HealthResponse(status="healthy")


@router.get("/ready", response_model=ReadyResponse)
def ready_check():
    """Check if the service is ready to accept requests."""
    # later: check database connection
    return ReadyResponse(status="ready")