FROM python:3.10

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

ENV PYTHONPATH="$PYTHONPATH:$PWD"

ENV PORT=${PORT}

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host","0.0.0.0", "--port", "8000"]

