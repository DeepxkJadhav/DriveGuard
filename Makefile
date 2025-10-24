# DriveGuard Makefile

run:
	docker-compose up --build

down:
	docker-compose down

backend:
	docker-compose up backend

frontend:
	docker-compose up frontend

mqtt:
	docker-compose up mqtt-broker

format:
	black services/**/*.py

test:
	pytest -v tests/
