FROM python:3.5

EXPOSE 8080

RUN mkdir -p /usr/src/app && pip install -U pip
WORKDIR /usr/src/app

COPY . /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]
