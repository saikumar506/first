FROM python:3.10

COPY . /app

WORKDIR /app

EXPOSE 6000

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
