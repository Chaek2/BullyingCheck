from fastapi import APIRouter,Response, Depends
from sqleditor import Sql, Tables
from fastapi import Body, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from Models.Tag_App import Tag_App
from auth.auth_bearer import JWTBearer

class Tag_AppController():
    router = APIRouter()


    @router.get("/")
    async def get() -> list[Tag_App]:
        item = Sql().select_all_table(Tables.Tag_App)
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(item))


    @router.get("/{id}")
    async def getBy(id: str) -> list[Tag_App]:
        item = Sql().select_one_table(Tables.Tag_App,id)
        if not item:
            return JSONResponse(
                status_code = status.HTTP_409_CONFLICT,
                content = { "message": "Error" }
        )
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(item))


    @router.post("/", dependencies=[Depends(JWTBearer())])
    async def post(data = Body()):
        item = Sql().post(Tables.Tag_App,data)
        if not item:
            return JSONResponse(
                status_code = status.HTTP_409_CONFLICT,
                content = { "message": "Error" }
        )
        return Response(status_code=status.HTTP_201_CREATED)


    @router.put("/{id}", dependencies=[Depends(JWTBearer())])
    async def put(id: str, data  = Body()) -> list[Tag_App]:
        item = Sql().put(Tables.Tag_App, data, id)
        if not item:
            return JSONResponse(
                status_code = status.HTTP_409_CONFLICT,
                content = { "message": "Error" }
        )
        item = Sql().select_one_table(Tables.Application, id)
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(item))


    @router.delete("/{id}", dependencies=[Depends(JWTBearer())])
    async def delete(id: str):
        item = Sql().delete(Tables.Tag_App, id)
        if not item:
            return JSONResponse(
                status_code = status.HTTP_409_CONFLICT,
                content = { "message": "Error" }
        )
        return Response(status_code=status.HTTP_200_OK)
