from typing import Annotated
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import csv
import codecs

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/files/upload")
async def create_file(file: UploadFile = File(...)):
    reader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
    data = []
    for row in reader:
        data.append(row)
        print(data)

    file.file.close()
    return data

# @app.post("/files")
# async def create_file(file: Annotated[bytes, File()]):
#     # with open(file, 'r') as csvfile:
#     #   reader = csv.DictReader(csvfile, dialect='exel')
#     #   for row in reader:
#     #      print(row)
#       return {"file-size": len(file)}