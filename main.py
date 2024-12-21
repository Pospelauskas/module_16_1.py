from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
def read_root():
    return HTMLResponse(content="<h2>Главная страница</h2>")


@app.get("/user/admin")
def read_admin():
    return HTMLResponse(content="Вы вошли как администратор")


@app.get("/user/{user_id}")
def read_user(user_id: int):
    return HTMLResponse(content=f"Вы вошли как пользователь № {user_id}")


@app.get("/user")
def read_user_info(username: str, age: int):
    return HTMLResponse(content=f"Информация о пользователе. Имя: {username}, Возраст: {age}")
