from pydantic import BaseModel
class Tag(BaseModel):
    Title: str

    def __init__(self, title: str):
        self.Title: str = title