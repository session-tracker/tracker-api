from pydantic import BaseModel
from pydantic.fields import Field


class Pong(BaseModel):
    default: str="App, version 0.0.1",
    title: str="pong",
    description: str="I'm alive"
