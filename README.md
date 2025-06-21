# Challenge Back-End – LQN 2025 🚀

Este proyecto es una API GraphQL + REST desarrollada con Django para fanáticos de **Star Wars**, cumpliendo los requerimientos del reto técnico de LQN 2025. Contiene documentación automática (Redoc).

---

## 📁 Estructura del proyecto

```
LQN-BACKEND/
├── core/
│   ├── models.py              # Planet, Film, Character
│   ├── schema.py              # GraphQL Schema
│   ├── serializers.py         # DRF serializers (anidados)
│   ├── views.py               # API Views
│   ├── templates/redoc.html   # Redoc UI template
│   └── static/redoc/          # Redoc JS (standalone)
├── starwars/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── Makefile
└── manage.py
```

---

## ⚙️ Instalación y ejecución (modo local)

### 1. Clona el repositorio

```bash
git clone https://github.com/rvosistemas/lqn-backend.git
cd lqn-backend
```

### 2. Construye el entorno Docker

```bash
make build
make up
```

> Esto levantará el backend de Django y lo expondrá en `http://localhost:8000/`.

---

## 📦 Dependencias principales

- Python 3.11
- Django 5.2
- Django REST Framework
- Graphene-Django
- drf-spectacular (para generar OpenAPI Schema)
- Pytest + Coverage (para pruebas)

---

## 🧠 Modelos principales

```python
class Planet(models.Model):
    name = models.CharField(max_length=100)

class Film(models.Model):
    title = models.CharField(max_length=100)
    opening_crawl = models.TextField()
    director = models.CharField(max_length=100)
    producers = models.CharField(max_length=255)
    planets = models.ManyToManyField(Planet)

class Character(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.CharField(max_length=10, blank=True)
    films = models.ManyToManyField(Film)
```

---

## 🔗 Endpoints disponibles

### REST

| Método | Endpoint           | Descripción       |
| ------ | ------------------ | ----------------- |
| GET    | `/api/planets/`    | Lista de planetas |
| POST   | `/api/films/`      | Crear película    |
| GET    | `/api/characters/` | Lista personajes  |

Los modelos anidados están disponibles en la respuesta (`films` dentro de `character`, `planets` dentro de `film`).

---

## 🧪 Documentación técnica

### Redoc UI

📍 [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

> Implementado mediante un `redoc.html` personalizado y `redoc.standalone.js` estático en `core/static/redoc/`.

---

## 🧬 GraphQL

### Interfaz (GraphiQL)

📍 [http://localhost:8000/graphql/](http://localhost:8000/graphql/)

Puedes consultar datos como:

```graphql
query {
  allCharacters {
    name
    birthYear
    films {
      title
      director
    }
  }
}
```

---

## ✅ Pruebas y cobertura

Este proyecto utiliza `pytest` junto con `pytest-cov` para ejecutar pruebas unitarias y generar reportes de cobertura.

### Ejecutar pruebas

```bash
make test
```

### Ejecutar pruebas con cobertura

```bash
make coverage
```

> Verás un reporte con líneas faltantes en el código. Ideal para asegurar calidad del proyecto.

---

## ♻️ Actualización automática del esquema

Cada vez que modificas los modelos o serializers, la documentación de Swagger y Redoc se actualiza automáticamente mediante `drf-spectacular`, sin necesidad de escribir el schema a mano.

---

## ✍️ Autor

- **Richard Vivas Ordoñez**
- Desarrollador Backend Fullstack
- [https://github.com/rvosistemas](https://github.com/rvosistemas)

---

## 🧼 Extras

- Soporte para Docker desde cero.
- Serializers anidados.
- Makefile para facilitar el uso.
- Ideal para expandirse con autenticación, permisos o más modelos Star Wars.