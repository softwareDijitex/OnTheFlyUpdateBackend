from fastapi import FastAPI, Request, UploadFile, HTTPException
from fastapi.responses import FileResponse, StreamingResponse
import tempfile
import os
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

@app.post("/v2/downloadFile/")
async def downlaod_file_multipart(request: Request):
    print("----> Download multipart file")
    filename = "JAQBBDSP_02.12.ufw"
    range_header = request.headers.get("range")
    file_size = os.path.getsize(filename)

    if range_header: 
        print("--> Request has range: ",range_header)
        try:
            range_start, range_end = range_header.strip().split("-")
            range_start = int(range_start)
            range_end = int(range_end) if range_end else file_size
            if range_end > file_size :
                range_end = file_size
        except ValueError:
            raise HTTPException(status_code=400, detail = "Invalid range header")

        if range_start > range_end:
            raise HTTPException(status_code=416, detail = "Requested range not satifiable. Start range should be less end range")
        
        if range_start > file_size:
            raise HTTPException(status_code=416, detail="Requested range not satifiable")

        range_length = (range_end - range_start)+1

        def multipart_file_read():
            with open(filename,"rb") as file:
                file.seek(range_start)
                bytes_read = 0
                while bytes_read < range_length:
                    chunk_size = min(1024 * 1024, range_length - bytes_read)
                    data = file.read(chunk_size)
                    if not data:
                        break
                    bytes_read += len(data)
                    yield data

        headers = {
            "Content-Range": f"bytes {range_start}-{range_end}/{file_size}",
            "Accept-Ranges": "bytes",
            }
        
        return StreamingResponse(multipart_file_read(), headers=headers, status_code=206)

    return FileResponse(filename)


         