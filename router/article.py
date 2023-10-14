from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import db_article
from db.database import get_db
from schemas import Article, ArticleBase, ArticleDisplay, ArticleUser
from auth.oauth2 import get_current_user, oauth2_scheme

router = APIRouter(prefix='/article',  tags=['Article'])

@router.post('/create', response_model= Article)
def createArticle(request:ArticleBase, db:Session=Depends(get_db)):
    return db_article.create_article(db=db, request=request)
    
@router.get('/{id}', response_model= ArticleUser)
#what matter most in response model is that key must be same thing
def getArticle(id:int,db:Session=Depends(get_db), currentuser:str=Depends(get_current_user)):
    article = db_article.get_article(id=id,db=db)
    return {'data':article, 'current_user':currentuser}
    # return{'status':'ok'}