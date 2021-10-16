FROM python:3.9

WORKDIR /apps/serega

COPY ./requirements.txt /apps/serega/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /apps/serega/requirements.txt

COPY . .