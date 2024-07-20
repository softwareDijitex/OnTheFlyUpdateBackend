from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse
import tempfile
# uploadedFile: tempfile


app = FastAPI()

@app.get("/") 
def get_latest_version():
    return {"version" : "1.0"}

# @app.post("/uploadFile")
# def upload_file(file: UploadFile):
#     print(file.file.read())
#     print("------> file format",file.filename.format)
#     # uploadedFile = tempfile(file.filename, file.file)
#     return {"filename" : file.filename,
#             "success" : "true" }

# @app.get("/getFile")
# def get_file():
#     return uploadedFile

@app.post("/downloadFile")
async def download_file():
    print("------> larger file sent")
    return FileResponse("JAQBBDSP_02.12.ufw")
