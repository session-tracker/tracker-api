from fastapi import APIRouter

from core.api.v1.endpoints import ping

router = APIRouter()
router.include_router(ping.router, tags=['ping'])