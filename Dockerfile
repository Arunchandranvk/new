FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /code 

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5050

CMD ["python","manage.py","runserver","0.0.0.0:5050"]
