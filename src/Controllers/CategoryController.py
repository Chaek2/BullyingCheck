from fastapi import APIRouter,Response, Depends
from sqleditor import Sql, Tables
from fastapi import Body, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from Models.Category import Category
from auth.auth_bearer import JWTBearer

class CategoryController():
    router = APIRouter()


    @router.get("/")
    async def get() -> list[Category]:
        item = Sql().select_all_table(Tables.Category)
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(item))


    @router.get("/{id}")
    async def getBy(id: str) -> list[Category]:
        item = Sql().select_one_table(Tables.Category,id)
        if not item:
            return JSONResponse(
                status_code = status.HTTP_409_CONFLICT,
                content = { "message": "Error" }
        )
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(item))


    @router.post("/", dependencies=[Depends(JWTBearer())])
    async def post(data = Body()):
        item = Sql().post(Tables.Category,data)
        if not item:
            return JSONResponse(
                status_code = status.HTTP_409_CONFLICT,
                content = { "message": "Error" }
        )
        return Response(status_code=status.HTTP_201_CREATED)


    @router.put("/{id}", dependencies=[Depends(JWTBearer())])
    async def put(id: str, data  = Body()) -> list[Category]:
        item = Sql().put(Tables.Category, data, id)
        if not item:
            return JSONResponse(
                status_code = status.HTTP_409_CONFLICT,
                content = { "message": "Error" }
        )
        item = Sql().select_one_table(Tables.Application, id)
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(item))


    @router.delete("/{id}", dependencies=[Depends(JWTBearer())])
    async def delete(id: str):
        item = Sql().delete(Tables.Category, id)
        if not item:
            return JSONResponse(
                status_code = status.HTTP_409_CONFLICT,
                content = { "message": "Error" }
        )
        return Response(status_code=status.HTTP_200_OK)
