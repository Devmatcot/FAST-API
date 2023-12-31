
import time
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from db import models
from fastapi.staticfiles import StaticFiles
from db.database import engine
from expection import StoryExpection
from router import blog_get, product, article, blog_post, user,file, dependencies
from auth import authentication

app = FastAPI()

app.include_router(authentication.router)
app.include_router(dependencies.router)
app.include_router(file.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(product.router)

@app.get('/', description='First endpoint')
def index():
    return 'Hello World'

@app.exception_handler(StoryExpection)
def story_expection_handler(request:Request,exc:StoryExpection):
    # that request is a must to be as parameter
    return JSONResponse(content={'status':False, 'message':exc.message},status_code=exc.statuscode,)
    

models.Base.metadata.create_all(engine)
# this is [mount] help to add statics files
app.mount(path='/files', app=StaticFiles(directory='files'), name='files')


# @app.middleware('http')
# async def add_middle_ware(request:Request, callnext):
#     start_time = time.time()
#     response = await callnext(request)
#     duration = time.time()-start_time
#     request.headers = str(duration)
#     return response
    