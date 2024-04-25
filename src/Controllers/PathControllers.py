from fastapi import APIRouter,Response, Depends, Body, UploadFile, File, status
from fastapi.responses import JSONResponse, FileResponse
from auth.auth_bearer import JWTBearer
import os.path
from pathlib import Path
import shutil

class PathControllers():
    router = APIRouter()

    @router.get("/")
    async def getBy(path = Body(embed=True)):
        nameapp = [i for i in os.listdir(path)]
        path += nameapp[0]
        name = nameapp[0]
        if os.path.exists(path):
            print(type(nameapp),type(name),name,path, 19)
            return FileResponse(path, media_type='application/octet-stream',filename=name)
        return JSONResponse(
            status_code = status.HTTP_418_IM_A_TEAPOT,
            content = { "message": "Нету файла" }
        )

    @router.post("/")
    async def post(file: UploadFile, path = Body(embed=True)):
        name = file.filename
        if path is not None:
            try:
                if os.path.exists(path):
                    return JSONResponse(
                        status_code = status.HTTP_418_IM_A_TEAPOT,
                        content = { "message": "Уже есть файл" }
                    )
                Path(path).mkdir(parents=True, exist_ok=True)
                with open(f'{path}{name}', 'wb') as f:
                    f.write(file.file.read())
                return Response("Создан",status_code=status.HTTP_201_CREATED)
            except Exception as e:
                print(e)
                return Response("Не повезло: "+str(e),status_code=status.HTTP_409_CONFLICT)
        return Response("Пусто",status_code=status.HTTP_404_NOT_FOUND)
                
    @router.delete("/")
    async def delete(path = Body(embed=True)):
        if path is not None:
            try:
                if os.path.exists(path):
                    return JSONResponse(
                        status_code = status.HTTP_418_IM_A_TEAPOT,
                        content = { "message": "Уже есть файл" }
                    )
                shutil.rmtree(path)
                return Response("Создан",status_code=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return Response("Не повезло: "+str(e),status_code=status.HTTP_409_CONFLICT)
        return Response("Пусто",status_code=status.HTTP_404_NOT_FOUND)