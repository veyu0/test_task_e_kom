FROM python:3

EXPOSE 8000

WORKDIR /app

RUN pip install fastapi uvicorn tinydb

COPY . .

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]