FROM python:3.10.6-buster

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN python -m pip install --upgrade pip
COPY requirements.txt /usr/src/app/
RUN export PYTHONPATH=/usr/bin/python \
 && pip install -r requirements.txt

COPY . /usr/src/app
CMD ["python3", "./main.py"]