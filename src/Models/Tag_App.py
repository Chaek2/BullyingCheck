from pydantic import BaseModel
class Tag_App(BaseModel):
    IDTagApp: int
    Tag: str
    Application: int

    def __init__(self, idtagapp: int, tag: str, application: int):
        self.IDTagApp: int = idtagapp
        self.Tag: str = tag
        self.Application: int = application