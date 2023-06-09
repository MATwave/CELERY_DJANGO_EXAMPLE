import time

from django.core.mail import send_mail
from loguru import logger

from celery_example.config import app_settings


class EmailSender:
    subject = 'Тестовое сообщение'
    message = 'Привет, это тестовое сообщение.'
    from_email = app_settings.email_host_user

    @classmethod
    def send_email(cls, email):
        logger.info('подожду немного и отправлю')
        time.sleep(100)  # имитация задержки
        send_mail(cls.subject, cls.message, cls.from_email, [email])
        logger.info('отправил')
