from pydantic import BaseModel
class Post(BaseModel):
    Title: str

    def __init__(self, title: str):
        self.Title: str = title