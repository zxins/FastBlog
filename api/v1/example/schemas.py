from typing import Optional

from pydantic import BaseModel


class ExampleSchema(BaseModel):
    name: str
