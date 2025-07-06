install:
	uv sync

build:
	chmod +x ./build.sh
	./build.sh

render-start:
	gunicorn task_manager.wsgi

lint:
	uv run ruff check

update_lang:
	uv run django-admin makemessages -l ru

compile_lang:
	uv run django-admin compilemessages

start-server:
	uv run python3 manage.py runserver

check:
	uv run ruff check

migrate:
	uv run python3 manage.py makemigrations
	uv run python3 manage.py migrate

collectstatic:
	uv run python manage.py collectstatic --noinput

compilemessages:
	uv run django-admin compilemessages

makemessages:
	uv run django-admin makemessages --ignore="static" --ignore=".env"  -l ru

test:
	uv run python3 manage.py test