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

run:
	uv run python3 manage.py runserver

check:
	uv run ruff check

migrate:
	uv run python3 manage.py makemigrations
	uv run python3 manage.py migrate

migrate_render:
	python3 manage.py makemigrations
	python3 manage.py migrate