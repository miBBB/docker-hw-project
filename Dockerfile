FROM python:3.12-alpine3.23
WORKDIR /srv/app/

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "web.py"]
