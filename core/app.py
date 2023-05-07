from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import get_config
from core.api.v1.api_router import router as api_v1_router

def get_application() -> FastAPI:
    project_name = get_config().project_name
    debug = get_config().debug
    version = get_config().version
    prefix = get_config().api_prefix
    openapi_url = get_config().openapi_url

    application = FastAPI(
        title=project_name,
        debug=debug,
        version=version,
        docs_url=None,
        redoc_url=None,
        openapi_url=openapi_url,
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=get_config().origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        
    )

    application.include_router(api_v1_router, prefix=get_config().api_prefix)

    return application