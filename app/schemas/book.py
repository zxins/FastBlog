from datetime import datetime
from pydantic import BaseModel


class BookSchema(BaseModel):
    id: int
    name: str
    access: int
    status: int
    brief: str
    publish_timestamp: datetime
    select_catalog: int
    cover: str
