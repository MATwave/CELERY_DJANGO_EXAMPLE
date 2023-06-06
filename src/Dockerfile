# Используйте базовый образ Python
FROM python:3.10

ENV PYTHONUNBUFFERED 1

# Установка зависимостей
WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

# Копирование файлов проекта
COPY . /app/

# Запуск приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
