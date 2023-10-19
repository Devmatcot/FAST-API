from fastapi import APIRouter, Depends, Request

router = APIRouter(prefix='/dependencies', tags=['Dependecies'])



def convert_header(request:Request, separator:str='----'):
    out_headers = []
    for key,value in request.headers.items():
        out_headers.append(f"{key} {separator} {value}")
    return out_headers


@router.get('')
def get_item(header=Depends(convert_header)):
    return {
        'items':['a','b','c'],
        'header':header
    }
    
@router.post('/new')
def creat_item(header=Depends(convert_header)):
    return {
        'result':'new item created',
        'header':header
    }


class Account():
    def __init__(self, name:str,email:str):
        self.name = name
        self.email = email

@router.post('/create')
def create_user(name:str,email:str,password:str,account:Account=Depends()):
    return{
        'name':account.name,
        'email':account.email
    }
