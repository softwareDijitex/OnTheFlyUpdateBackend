# # syntax=docker/dockerfile:1

# FROM python:3.10

# WORKDIR /code

# COPY requirements.txt /code/requirements.txt

# RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# COPY . /code

# #EXPOSE 8000

# #CMD ["gunicorn", "main:app"]
# CMD ["fastapi", "run", "main.py", "--port", "80"]