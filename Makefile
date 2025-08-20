# docker
docker-build:
	docker-compose up --build

docker-build-and-migrate:
	docker-compose up --build -d
	@echo "Waiting for database to be ready..."
	@for i in {1..30}; do \
		if docker exec okpos_test-db-1 pg_isready -U postgres -d postgres >/dev/null 2>&1; then \
			echo "Database is ready!"; \
			break; \
		else \
			echo "Waiting for database... ($$i/30)"; \
			sleep 2; \
		fi; \
		if [ $$i -eq 30 ]; then \
			echo "Database failed to start in 60 seconds"; \
			exit 1; \
		fi; \
	done
	docker exec -it okpos_test-web-1 /bin/bash -c \
	"python3 manage.py makemigrations && \
	python3 manage.py migrate"

docker-prune-all:
	docker-compose down
	docker system prune -a --volumes -f
	rm -rf postgres_data

# django
migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

createsuperuser:
	python3 manage.py shell -c "from django.contrib.auth import get_user_model; \
	User = get_user_model(); \
	u, created = User.objects.get_or_create(username='root', defaults={'email':'root@test.com','is_staff':True,'is_superuser':True}); \
	u.set_password('root'); \
	u.save(); \
	print('created' if created else 'updated')"

# reset
reset-db:
	rm -rf db.sqlite3
	make migrate

reset-local-server:
	make reset-db
	make createsuperuser
	python manage.py runserver
