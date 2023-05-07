import uvicorn

from core.app import get_application
from core.config import get_config

if __name__ == '__main__':
    app = get_application()
    uvicorn.run(
        app,
        host=get_config().host,
        port=get_config().port,
    )
