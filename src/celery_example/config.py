from dotenv import load_dotenv
from pydantic import BaseSettings
from pydantic import Field


class AppSettings(BaseSettings):
    secret_key: str = Field(..., env='SECRET_KEY')
    email_host: str = Field(..., env='EMAIL_HOST')
    email_port: int = Field(..., env='EMAIL_PORT')
    email_host_user: str = Field(..., env='EMAIL_HOST_USER')
    email_host_password: str = Field(..., env='EMAIL_HOST_PASSWORD')
    debug: bool = Field(default=False, env='DJANGO_DEBUG')
    redis_host: str = Field(..., env='REDIS_HOST')
    redis_port: int = Field(..., env='REDIS_PORT')

    @classmethod
    def load(cls):
        load_dotenv('.env')
        return cls()

    @property
    def redis_url(self) -> str:
        return f'redis://{self.redis_host}:{self.redis_port}'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


app_settings = AppSettings.load()
