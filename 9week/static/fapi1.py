from fastapi import FastAPI, Form, File, UploadFile
from fastapi.staticfiles import StaticFiles
import uvicorn
from typing import List, Tuple
import shutil
from pathlib import Path


app = FastAPI()


app.mount("/static", StaticFiles(directory="static", html=True), name="static")


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    save_path = Path("static/uploads") / file.filename
    save_path.parent.mkdir(parents=True, exist_ok=True)
    
    with save_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return {"filename": file.filename, "location": str(save_path)}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/item")
def read_item(item_id: int, name: str = None, age: int = 0):
    return {"item_id": item_id, "name": name, "age": age}


@app.post("/user")
async def read_user_form(
    name: str = Form(...), 
    studentcode: str = Form(...), 
    major: str = Form(...)
):
    return {"msg": f"{major} {name}님 ({studentcode}) 반갑습니다."}


@app.post("/plus")
async def plus(numbers: List[Tuple[int, int]]):
    results = [f"{num1} + {num2} = {num1 + num2}" for num1, num2 in numbers]
    return {"result": " | ".join(results)}


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000, log_level="info")
