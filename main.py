import fastapi
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://localhost:8001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/login")
async def root(request: fastapi.Request):
    data = await request.json()
    username = data.get("username")
    password = data.get("password")
    if username is not None and password is not None:
        return {"message": "Login successful!"}
    else:
        return {"message": "Invalid username or password"}
