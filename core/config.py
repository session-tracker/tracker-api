from pydantic import BaseSettings
from typing import Any, Dict, List


class AppConfig(BaseSettings):
    host: str = 'localhost'
    port: int = 5000
    project_name: str = 'Session Tracker API'
    api_prefix: str = '/api/v1'
    version: str = '1.0.0'
    openapi_url: str = '/docs/v1/openapi.json'
    docs_url: str = '/docs/v1/'
    debug: bool = False
    origins: List[str] = [
        "*",
    ]

def get_config() -> AppConfig:
    return AppConfig()