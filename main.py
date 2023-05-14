import uvicorn

from core.app import get_application
from core.config import get_config

app = get_application()

if __name__ == '__main__':
    uvicorn.run(
        app,
        host=get_config().host,
        port=get_config().port,
    )
