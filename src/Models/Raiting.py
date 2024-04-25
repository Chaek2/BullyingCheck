from pydantic import BaseModel
class Raiting(BaseModel):
    IDRaiting: int
    Email: str
    Application: int
    Value: float

    def __init__(self, idraiting: int, email: str, application: int, value: float):
        self.IDRaiting: int = idraiting
        self.Email: str = email
        self.Application: int = application
        self.Value: float = value