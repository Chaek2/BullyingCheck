from pydantic import BaseModel
class Feedback(BaseModel):
    IDFeedback: int
    Email: str
    Application: int
    Message: str
    Dates: str
    Answer: int

    def __init__(self, idfeedback: int, email: str, application: int, message: str, dates: str, answer: int):
        self.IDFeedback: int = idfeedback
        self.Email: str = email
        self.Application: int = application
        self.Message: str = message
        self.Dates: str = dates
        self.Answer: int = answer
