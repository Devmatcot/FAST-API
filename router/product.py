import time
from typing import Optional
from fastapi import APIRouter, Header, Response

router = APIRouter(prefix='/product', tags=['Product'])


product = ['food', 'cloth', 'bag']
# learning about concurrency in FAST API
async def time_consuming_function():
    time.sleep(3)

@router.get('/all')
async def get_all_product():
    await time_consuming_function()
    return product

#learning about header in Fast API

@router.get('/withheader')
def get_product(response:Response, custom_header:Optional[str]=Header(None)):
    return product
    