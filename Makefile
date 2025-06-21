# Makefile para el proyecto Django LQN Backend

# Ejecutar todas las pruebas
test:
	docker compose run --rm web pytest

# Ejecutar pruebas con reporte de cobertura
coverage:
	docker compose run --rm web pytest --cov=core --cov-report=term-missing

# Levantar entorno de desarrollo
up:
	docker compose up

# Reconstruir imagen de Docker
build:
	docker compose build

# Apagar entorno
down:
	docker compose down

# Reiniciar solo el contenedor web
restart:
	docker compose restart web

# Acceso al contenedor web con bash
shell:
	docker compose exec web bash
