from fastapi import APIRouter,Response, Depends
from sqleditor import Sql, Tables
from fastapi import Body, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from Models.Application import Application
from auth.auth_bearer import JWTBearer

class ApplicationController():
    router = APIRouter()


    @router.get("/")
    async def get() -> list[Application]:
        item = Sql().select_all_table(Tables.Application)
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(item))


    @router.get("/{id}")
    async def getBy(id: str) -> list[Application]:
        item = Sql().select_one_table(Tables.Application,id)
        if not item:
            return JSONResponse(
                status_code = status.HTTP_409_CONFLICT,
                content = { "message": "Error" }
        )
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(item))


    @router.post("/", dependencies=[Depends(JWTBearer())])
    async def post(data = Body()):
        item = Sql().post(Tables.Application,data)
        if not item:
            return JSONResponse(
                status_code = status.HTTP_409_CONFLICT,
                content = { "message": "Error" }
        )
        return Response(status_code=status.HTTP_201_CREATED)


    @router.put("/{id}", dependencies=[Depends(JWTBearer())])
    async def put(id: str, data  = Body()) -> list[Application]:
        item = Sql().put(Tables.Application, data, id)
        if not item:
            return JSONResponse(
                status_code = status.HTTP_409_CONFLICT,
                content = { "message": "Error" }
        )
        item = Sql().select_one_table(Tables.Application, id)
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(item))


    @router.delete("/{id}", dependencies=[Depends(JWTBearer())])
    async def delete(id: str):
        item = Sql().delete(Tables.Application, id)
        if not item:
            return JSONResponse(
                status_code = status.HTTP_409_CONFLICT,
                content = { "message": "Error" }
        )
        return Response(status_code=status.HTTP_200_OK)
