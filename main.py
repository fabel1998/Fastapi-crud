from fastapi import FastAPI
import uvicorn

from databases import engine, Base
from routers import blog, user, login


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(login.router)
app.include_router(blog.router)
app.include_router(user.router)

if __name__ == '__main__':
	uvicorn.run(app, host='127.0.0.1', port=8000)