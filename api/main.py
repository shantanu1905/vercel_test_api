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



@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/signup", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("create_user.html", {"request": request})

@app.get("/activate_account", name="activate_account",response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("generate_otp.html", {"request": request})

@app.get("/verify_account", name="verify_account",response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("verify_account.html", {"request": request})

@app.get("/login", name="login",response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/profile", name="profile",response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0")
