from typing import Optional
from fastapi import APIRouter, Header, Response

router = APIRouter(prefix='/product', tags=['Product'])


product = ['food', 'cloth', 'bag']
@router.get('/all')
def get_all_product():
    return product


#learning about header in Fast API


@router.get('/withheader')
def get_product(response:Response, custom_header:Optional[str]=Header(None)):
    
    return product
    