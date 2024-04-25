import uvicorn
import logging
from fastapi import FastAPI, Response,status
from Controllers.ApplicationController import ApplicationController
from Controllers.CategoryController import CategoryController
from Controllers.Category_AppController import Category_AppController
from Controllers.FeedbackController import FeedbackController
from Controllers.PersonController import PersonController
from Controllers.PostController import PostController
from Controllers.RaitingController import RaitingController
from Controllers.TagController import TagController
from Controllers.Tag_AppController import Tag_AppController
from Controllers.GoogleControllers import GoogleControllers
from Controllers.PathControllers import PathControllers
from starlette.middleware.sessions import SessionMiddleware
from decouple import config as cf

FORMAT = ""
logging.basicConfig(format=FORMAT, level=logging.INFO)
log = logging.getLogger("reucloud")
log.info("\tasctime\t \t-   name     -\t levelname \t- \tmessage\t")

app = FastAPI(title='REUCloud',description='Облачное хранение',version='1.0.1')
app.add_middleware(SessionMiddleware, secret_key="Oe_Ef1Y38o1KSWM2R-s-Kgfdsfy654y")

@app.get("/")
async def get():
    return Response("API START",status_code=status.HTTP_200_OK)


app.include_router(GoogleControllers.router, tags=["google"])
app.include_router(PathControllers.router, prefix="/path", tags=["path"])
app.include_router(ApplicationController.router, prefix="/application",tags=["application"])
app.include_router(CategoryController.router, prefix="/category",tags=["category"])
app.include_router(Category_AppController.router, prefix="/category_app",tags=["category_app"])
app.include_router(FeedbackController.router, prefix="/feedback",tags=["feedback"])
app.include_router(PersonController.router, prefix="/person",tags=["person"])
app.include_router(PostController.router, prefix="/post",tags=["post"])
app.include_router(RaitingController.router, prefix="/raiting",tags=["raiting"])
app.include_router(TagController.router, prefix="/tag",tags=["tag"])
app.include_router(Tag_AppController.router, prefix="/tag_app",tags=["tag_app"])

if __name__ == "__main__":
    uvicorn.run(app, port=5062,host='0.0.0.0', log_config='app/log_conf.yaml')