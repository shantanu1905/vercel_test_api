from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from database import Base , engine
from routers import auth


app = FastAPI()
templates = Jinja2Templates(directory="templates")
Base.metadata.create_all(engine)
app.include_router(auth.router)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0")
