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
	uv run django-admin makemessages --all

compile_lang:
	uv run django-admin compilemessages