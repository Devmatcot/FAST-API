from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from db.hash import Hash
from db.models import DbUser
from schemas import UserBase


def create_user(db:Session, request:UserBase):
    new_user = DbUser(
        username = request.username,
        email= request.email,
        password= Hash.bcrypt(request.password)
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#read all user from database
def get_all_user(db:Session):
    return db.query(DbUser).all()

#read a single user/element from database
def get_user(db:Session,id:int):
    user = db.query(DbUser).filter(DbUser.id ==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'user  with {id} not found')
    return user


#get user by username
def get_user_by_username(db:Session,username:str):
    user = db.query(DbUser).filter(DbUser.username ==username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'user  with username {username} not found')
    return user



#update query in Database

def update_user(id:int, db:Session,request:UserBase):
    user = db.query(DbUser).filter(DbUser.id==id)
    #TODO: Handle Expection
    user.update({
        DbUser.username:request.username,
        DbUser.email:request.email,
        DbUser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return {'status':'ok'}



def delete_user(id:int, db=Session):
    #TODO: Handle Expection
    user = db.query(DbUser).filter(DbUser.id==id).first()
    db.delete(user)
    db.commit()
    return {'status':'operation sucessful'}
    
    