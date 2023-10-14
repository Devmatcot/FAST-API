from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import db_user
from db.database import get_db

from schemas import UserBase, UserDisplay


router = APIRouter(prefix='/user',tags=['User'])

#create user 
@router.post('/create', response_model= UserDisplay)
def createAccount(request:UserBase, db:Session = Depends(get_db),):
    return db_user.create_user(request=request, db=db)


#update! 

#read all user
@router.get('/alluser', response_model= list[UserDisplay])
def getAllUser(db:Session= Depends(get_db),):
    return db_user.get_all_user(db= db)

#read single user from db
@router.get('/{id}', response_model= UserDisplay)
def getUser(id:int,db:Session = Depends(get_db),):
    return db_user.get_user(db=db, id=id)
    
#update user endpoint
@router.post('/update/{id}')
def updateUser(id:int,request:UserBase,db:Session=Depends(get_db)):
    return db_user.update_user(id=id,request=request, db=db)
    

#delete user
@router.delete('/delete/{id}')
def deleteUser(id:int,db:Session=Depends(get_db)):
    return db_user.delete_user(db=db, id=id)

    