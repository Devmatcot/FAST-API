from fastapi import APIRouter,Response, status
from typing import Optional
from enum import Enum



router = APIRouter(prefix='/blog', tags=['Blog'])

class BlogType(Enum):
    short='short'
    story='story'
    howto='howto'

@router.get('/all')
def getAllBlog(page=1,page_size: Optional[int]= None):
    return {'message':f"All {page_size} blog on page {page}"}

@router.get('/type/{type}' )
def getBlogType(blog:BlogType):
    return {'message': f"Blog Type {blog}"}


#combine query and path parameter together
@router.get('/{id}/comment/{comment_id}', tags=['Comment'])
def getBlogComment(id:int,comment_id,username:str,valid:Optional[bool]=False,):
    return {'message':f"blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}"}


@router.get('/{id}')
def getBlog(id:int, response:Response):
    if id>5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'status': False,'message':f'blog {id} not found'}
    else:
        response.status_code =status.HTTP_200_OK
        return {'message':f"This is blog post {id}"}