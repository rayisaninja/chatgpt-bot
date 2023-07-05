from beanie import Document
from pydantic import Field

class User(Document):
    id: int = Field(alias="_id", default=None)
    first_name: str
    last_name: str | None = Field(default=None)
    token_limit: int = Field(default=500)
    subscribed: bool = Field(default=False)
    subscribe_checked = Field(default=False)

    class Settings:
        name = "user"
