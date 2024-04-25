from pydantic import BaseModel
class Application(BaseModel):
    IDApplication: int
    Title: str
    Author: str
    Image: str
    Description: str

    def __init__(self, idapplication: int, title: str, author: str, image: str, description: str):
        self.IDApplication: int = idapplication
        self.Title: str = title
        self.Author: str = author
        self.Image: str = image
        self.Description: str = description
