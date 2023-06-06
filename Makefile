ADMIN_PANEL_DOCKER_COMPOSE_FILE = -f docker-compose.yml

up:
	# Запуск контейнеров Docker в фоновом режиме и перестройка образов, если необходимо
	docker compose $(APP_DOCKER_COMPOSE_FILE) up -d --build || \
		(echo "Failed to start containers" && exit 1)
	# Ожидание, пока контейнер admin_panel станет здоровым
	until [ "$$(docker inspect -f '{{.State.Health.Status}}' webapp)" = "healthy" ]; do \
		sleep 1; \
	done

	# Выполнение миграций базы данных внутри контейнера
	docker exec -i webapp bash -c "python manage.py migrate" || \
		(echo "Failed to run migrations" && exit 1)

	# Создание суперпользователя
	-docker exec -i webapp python  manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin')"  && \
    echo "Superuser created successfully." || \
    (echo "Failed to create superuser" && exit 1)

down:
	docker compose $(APP_DOCKER_COMPOSE_FILE) down -v
