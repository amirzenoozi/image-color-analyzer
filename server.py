from typing import Optional
from datetime import datetime
from fastapi import FastAPI, UploadFile
from script.analyzer import preprocess, analyze
from script.utils import save_file

import cv2
import os

app = FastAPI()


@app.get("/")
def read_root():
    return 'Hello World!'


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.post("/uploadfile/")
def create_upload_file(image: UploadFile):
    if not image:
        return {"message": "No upload file sent"}
    else:
        if not os.path.exists("upload"):
            os.mkdir("upload")
        
        file_parts = image.filename.split(".")
        date = str(datetime.timestamp(datetime.now())).replace(".", "-")
        file_name = f'{os.getcwd()}\\upload\\{file_parts[0].replace(" ", "-")}_{date}.{file_parts[1]}'
        save_file(file_name, image.file.read())
        
        img = cv2.imread(file_name)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        modified_image = preprocess(img)
        _, color = analyze(modified_image, args=None)

        return {"color": color}