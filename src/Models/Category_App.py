from pydantic import BaseModel
class Category_App(BaseModel):
    IDCategoryApp: int
    Category: str
    Application: int

    def __init__(self, idcategoryapp: int, category: str, application: int):
        self.IDCategoryApp: int = idcategoryapp
        self.Category: str = category
        self.Application: int = application
