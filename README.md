# CELERY_DJANGO_EXAMPLE

используется:
- django
- celery(redis)
- flower

___

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
