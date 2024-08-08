include ./tools/env/dev.env
export

default: run

run: start

start:
	docker compose up -d

stop:
	docker compose down

logs:
	docker compose logs -tf

build: docker-build collectstatic migrate

docker-build:
	docker compose build

collectstatic:
	docker compose run --rm cli python manage.py collectstatic --noinput

migrate:
	docker compose run --rm cli python manage.py migrate ${app_name}

load-initial-fixtures:
	docker-compose run --rm cli python manage.py loaddata /app/fixtures/initial_data.json

export-fixtures:
	@docker compose run --rm cli python manage.py dumpdata --format=json

makemigrations:
	docker compose run --rm cli python manage.py makemigrations ${app_name}

flush-db:
	docker compose run --rm cli python manage.py flush --noinput

reset-db:
	docker compose run --rm cli python manage.py reset_db -c --noinput

createsuperuser:
	docker compose run --rm cli python manage.py createsuperuser

cli:
	docker compose run --rm cli sh

purge:
	docker compose down -v --remove-orphans
	rm -rf ./static/*

app:
	docker compose run --rm cli python manage.py startapp ${app_name}

test:
	docker compose run --rm cli python manage.py test