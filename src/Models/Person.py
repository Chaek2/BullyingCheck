from pydantic import BaseModel
class Person(BaseModel):
    Email: str
    Code: str
    Surname: str
    Name: str
    Post: str
    Image: str

    def __init__(self, email: str, code: str, surname: str, name: str, post: str, image: str):
        self.Email: str = email
        self.Code: str = code
        self.Surname: str = surname
        self.Name: str = name
        self.Post: str = post
        self.Image: str = image