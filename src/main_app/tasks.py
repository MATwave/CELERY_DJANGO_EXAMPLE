from .service import EmailSender
from celery_example.celery import app


@app.task
def send_test_email(user_email):
    EmailSender.send_email(user_email)
