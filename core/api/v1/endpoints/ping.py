from fastapi import APIRouter

from core.api.v1.models.pong import Pong
from core.config import get_config

router = APIRouter()

@router.get("/ping", response_model=Pong)
async def ping() -> Pong:
    return Pong(
        default=get_config().project_name,
        title=get_config().version
    )
