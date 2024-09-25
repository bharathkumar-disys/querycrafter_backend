from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    CustomerName: str
    UserName: str
    Email: str
    Password : str


class UserLogin(BaseModel):
    username:str
    password:str
    
class Userresponseforviz(BaseModel):
    message:str
    connection_string:str
    
class Userquestions(BaseModel):
    connection_string:str
    role: Optional[str] = None
    
class ErrorFeedback(BaseModel):
    database_name:str
    role:str
    question:str
    feedback:Optional[str] = None
    rolerating: int
    questionrating: int
    queryrating: int
    vizrating: int


