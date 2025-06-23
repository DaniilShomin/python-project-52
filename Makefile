install:
	uv sync

PORT ?= 8000

build:
	chmod +x ./build.sh
	./build.sh

render-start:
	gunicorn task_manager.wsgi

lint:
	uv run ruff check