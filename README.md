# CELERY_DJANGO_EXAMPLE
Небольшое приложение на джанге. На главной странице форма для отправки тестового сообщения на почту. Реализация с иметацией задержки для наглядной демонстрации разницы работы с Celery. С Celery задача не блокируется, а выносится в фон. Плюсом поднят Flower для визуализации фоновых задач  

---

используется:
- django
- celery(redis)
- flower

---

!!! важно !!!
укажи валидные данные в файле переменных окружения .env.template (EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)

поднять:
```makefile
make up
```
остановить:
```makefile
make down
```
---

<details><summary>ДЛЯ РАЗРАБОТКИ</summary>

Находясь в корне проекта - включи пре-коммит

  ```commandline
  pre-commit install
  pre-commit autoupdate
  ```

Проверь работоспособность

  ```commandline
  pre-commit run --all-files
  ```

</details>

---
