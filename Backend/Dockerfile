FROM python:3.9

WORKDIR /kalato

COPY ./requirements.txt /kalato/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /kalato/requirements.txt

COPY ./app /kalato/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
