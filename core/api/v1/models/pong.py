from pydantic import BaseModel
from pydantic.fields import Field


class Pong(BaseModel):
    default: str="App, version X.Y.Z",
    title: str="pong",
    description: str="I'm alive"
