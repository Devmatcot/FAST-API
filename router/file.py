from fastapi import APIRouter, File, UploadFile
import shutil
from fastapi.responses import FileResponse




router = APIRouter(prefix='/file', tags=['File'])

@router.post('/upload')
def get_file(file:bytes=File(...)):
    content = file.decode()
    line = content.split('\n')
    return {'lines':line}
    
@router.post('/uploadfile')
def upload_file(uploadfile:UploadFile=File(...)):
    path = f'files/{uploadfile.filename}'
    with open (path,'w+b') as buffer:
        shutil.copyfileobj(uploadfile.file,buffer)
    return {'filename':path, 'type':uploadfile.content_type}
    

@router.get('/download/{name}', response_class= FileResponse)
def download_file(name:str):
    path = f'files/{name}'
    return path

