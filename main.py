from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"Olá" : "Mundo"}

class User(BaseModel):
    id: int
    email: str
    passw: str

data_users = [
    User(id = 1, email = "a@a.com", passw = "asd"),
    User(id = 2, email = "b@b.com", passw = "fgh")
]

@app.get("/users")
def getUsers():
    return data_users

@app.get("/users/{id}")
def getUserId(id: int):
    for user in data_users:
        if(user.id == id):
            return user

    return {"Status": 404, "Msg": "Not found"}

@app.post("/user/add")
def addUser(user: User):
    data_users.append(user)
    return user