from typing import Annotated
from fastapi import FastAPI, UploadFile, File
import csv
import codecs

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/files/upload")
async def create_file(file: UploadFile = File(...)):
    reader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
    data = {}
    for row in reader:
        key = row["First Name"]
        data[key] = row
        print(row["First Name"], row["Mobile Phone"])

    file.file.close()
    return data

# @app.post("/files")
# async def create_file(file: Annotated[bytes, File()]):
#     # with open(file, 'r') as csvfile:
#     #   reader = csv.DictReader(csvfile, dialect='exel')
#     #   for row in reader:
#     #      print(row)
#       return {"file-size": len(file)}