from pydantic import BaseModel


#this [class Config() orm_mode=True} always determing how the endpoint response will be represent

class UserBase(BaseModel):
    username:str
    email:str
    password:str

class User(BaseModel):
    id:int
    username:str
    class Config():
        orm_mode =True


#Article inside user display
class Article(BaseModel):
    title:str
    content:str
    published:bool
    class Config():
        orm_mode=True

class ArticleBase(BaseModel):
    title:str
    content:str
    published:bool
    creator_id:int

class ArticleDisplay(BaseModel):
    title:str
    content:str
    published:bool
    user:User
    class Config():
        from_attributes =True


class UserDisplay(BaseModel):
    username:str
    email:str
    item:list[Article]=[]
    class Config():
        from_attributes = True

class ArticleUser(BaseModel):
    data:ArticleDisplay
    current_user:UserDisplay
    class Config():
        from_attributes:True