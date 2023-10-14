from typing import List, Optional
from fastapi import APIRouter, Body, Query
from pydantic import BaseModel

router = APIRouter(prefix='/blog', tags=['Blog'])



class BlogModel(BaseModel):
    title:str
    content:str
    published:Optional[bool]=False

@router.post('/new')
def createBlog(blog:BlogModel):
    return blog

@router.post('/fecth/{id}')
def fecthBlog(blog:BlogModel, id:int, version:int=1):
    return {
        'id':id,
        'data': blog,
        'version':version
    }

#parameter metadata Query(), Body(), Path() [Body(...) it mean elipses and it is a required body]
@router.post('/post_comment/{id}')
def createComment(
                  blog:BlogModel,
                  id:int,comment_id:int=Query(None, description='Create new comment on the post'),
                  content:str = Body('Today is a good day', description=' This request body is optional'),
                  status: str= Body(..., min_length=10),
                  v: Optional[List[str]]= Query(['1.2','1.0'], description='list of version')
                  ):
    return {
        "id":id,
        'data':blog,
        'comment_id':comment_id,
        'content':content,
        'status':status,
        'version':v
    }
    