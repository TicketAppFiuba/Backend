FROM python:3.7.4

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

RUN export PYTHONPATH="$PYTHONPATH:$PWD"

ENV PORT $PORT
EXPOSE $PORT

CMD ["uvicorn", "main:app", "--host","0.0.0.0", "--port", "8000"]

# CMD pytest

