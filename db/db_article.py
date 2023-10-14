from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from db.models import DbArticle
from expection import StoryExpection
from schemas import ArticleBase


def create_article(db:Session, request:ArticleBase):

    if request.content.startswith('Once upon a time'):
        raise StoryExpection(message='No Story please add a detailed content', statuscode=418)
        
    new_article = DbArticle(user_id=request.creator_id, title=request.title, published=request.published, content= request.content)
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article
    

def get_article(id:int,db:Session):
    article = db.query(DbArticle).filter(DbArticle.id==id).first()
    #Handle expection
    # if not article:
    #     raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f'Article with id {id} not found')
    if not article:
        raise StoryExpection(message=f'Article with id {id} not found', statuscode=status.HTTP_404_NOT_FOUND)
    else:
        return article
    