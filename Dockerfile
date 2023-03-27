FROM python:3.7.4

COPY . /app
WORKDIR /app

RUN pip install poetry
RUN poetry install

ENV PORT $PORT
EXPOSE $PORT

CMD ["poetry","run","uvicorn", "main:app", "--host","0.0.0.0", "--port", "8000"]

