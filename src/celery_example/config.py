import os

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class AppSettings(BaseSettings):
    secret_key: str = os.getenv('SECRET_KEY')
    email_host: str = os.getenv('EMAIL_HOST')
    email_port: int = os.getenv('EMAIL_PORT')
    email_host_user: str = os.getenv('EMAIL_HOST_USER')
    email_host_password: str = os.getenv('EMAIL_HOST_PASSWORD')

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


app_settings = AppSettings()
