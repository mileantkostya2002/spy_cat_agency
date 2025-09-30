# spy_cat_agency# 🐾 Spy Cats Service API

**Spy Cats Service** is a REST API for managing secret cat agents, their missions, and their targets.
The project is built with **Django + DRF**, supports **JWT authentication**, and includes interactive **Swagger documentation**.

---

## ✨ Features

* **Spy Cats Management**

  * Name, breed, years of experience, salary 🐱

* **Mission Management**

  * Assign cats to missions
  * Track completion status 🎯

* **Target Management**

  * Store details such as name, country, notes
  * Prevent modifications to completed targets

* **Breeds Management** 🐾

* **User Authentication**

  * JWT-based authentication for secure access

* **Interactive API Docs**

  * Swagger / OpenAPI documentation generated with `drf-spectacular`

---

## 🛠️ Tech Stack

* [Python 3.12+](https://www.python.org/)
* [Django 5.2.5](https://www.djangoproject.com/)
* [Django REST Framework](https://www.django-rest-framework.org/)
* [drf-spectacular](https://drf-spectacular.readthedocs.io/) — OpenAPI/Swagger docs
* [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/) — Authentication
* [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/)

---

## ⚙️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/mileantkostya2002/spy_cat_agency
cd spy-cats-service

# You can use the fixture to see the data
python manage.py loaddata spy_cat_fixtures.json

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # for Linux/Mac
venv\Scripts\activate     # for Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create a superuser (for Django admin)
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```

---

## 🔑 Authentication

This project uses **JWT (JSON Web Tokens)** for authentication.
Obtain tokens via:

```
POST /api/token/
```

Refresh tokens via:

```
POST /api/token/refresh/
```

Use the token in the `Authorization` header:

```
Authorization: Bearer <your_token>
```

---

## 📖 API Documentation

Once the server is running, explore the interactive docs:

* Swagger UI: [http://localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/)
* ReDoc: [http://localhost:8000/api/schema/redoc/](http://localhost:8000/api/schema/redoc/)

---

```

---
## 🐾 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute it as you like.
