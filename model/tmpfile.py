from fastapi import UploadFile
class tmpfile:
    def __init__(self, filename : str, file : UploadFile):
        self.filename = filename
        self.file = file