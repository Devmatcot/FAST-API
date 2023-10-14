from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db.database import get_db
from db.hash import Hash
from db.models import DbUser
from auth import oauth2

router = APIRouter(tags=['Authentication'])

@router.post('/token')
def get_token(request:OAuth2PasswordRequestForm =Depends(), db:Session = Depends(get_db)):
    user = db.query(DbUser).filter(DbUser.username ==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid credential')
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect email or password')

    access_token = oauth2.create_access_token(data={'sub':user.username})
    return {
        'access_token':access_token,
        'token_type':'bearer',
        'user_id':user.id,
        'username':user.username
    }