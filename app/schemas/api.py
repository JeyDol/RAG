from pydantic import BaseModel


class UploadRequest(BaseModel):
    text: str

class AskRequest(BaseModel):
    question: str