📦 Inventory Management API

Español abajo

A REST API built with FastAPI and SQLAlchemy to manage product stock and sales for small businesses. Designed as a backend portfolio project with clean architecture, input validation, and automated tests.

🛠️ Tech Stack

Python 3.10+
FastAPI — modern, high-performance web framework
SQLAlchemy — ORM for database management
SQLite — lightweight local database
Pydantic v2 — data validation and serialization
Pytest — automated testing



📁 Project Structure
inventario/
├── app/
│   ├── main.py          # App entry point, router registration
│   ├── models.py        # SQLAlchemy database models
│   ├── schemas.py       # Pydantic schemas with validation
│   ├── crud.py          # Database operations layer
│   ├── database.py      # DB connection and session management
│   └── routers/
│       ├── products.py  # Product endpoints
│       └── sales.py     # Sales endpoints
└── tests/
├── test\_products.py
└── test\_sales.py

🚀 Getting Started

1. Clone the repository
bashgit clone https://github.com/Shaco10/inventory-api.git
cd inventory-api
2. Install dependencies
bashpip install fastapi sqlalchemy uvicorn httpx pytest pydantic
3. Run the server
bashuvicorn app.main:app --reload

On Windows with Python from the Microsoft Store, use py -m uvicorn app.main:app --reload

4. Open the interactive docs
http://127.0.0.1:8000/docs

🔌 API Endpoints
📦 Inventory Management API

Español abajo

A REST API built with FastAPI and SQLAlchemy to manage product stock and sales for small businesses. Designed as a backend portfolio project with clean architecture, input validation, and automated tests.

🛠️ Tech Stack

Python 3.10+

FastAPI — modern, high-performance web framework

SQLAlchemy — ORM for database management

PostgreSQL — relational database hosted on Railway

Pydantic v2 — data validation and serialization

Pytest — automated testing

📁 Project Structure

inventario/

├── app/

│   ├── main.py          # App entry point, router registration

│   ├── models.py        # SQLAlchemy database models

│   ├── schemas.py       # Pydantic schemas with validation

│   ├── crud.py          # Database operations layer

│   ├── database.py      # DB connection and session management

│   └── routers/

│       ├── products.py  # Product endpoints

│       └── sales.py     # Sales endpoints

└── tests/

├── test\_products.py

└── test\_sales.py

🚀 Getting Started



Clone the repository

bashgit clone https://github.com/Shaco10/inventory-api.git

cd inventory-api

Install dependencies

bashpip install fastapi sqlalchemy uvicorn httpx pytest pydantic

Run the server

bashuvicorn app.main:app --reload



On Windows with Python from the Microsoft Store, use py -m uvicorn app.main:app --reload



Open the interactive docs

http://127.0.0.1:8000/docs



🔌 API Endpoints

Products

MethodEndpointDescriptionPOST/products/Create a new productGET/products/List all productsPUT/products/{id}Update a productDELETE/products/{id}Delete a product

Sales

MethodEndpointDescriptionPOST/sales/Register a sale (reduces stock automatically)GET/sales/List all sales

✅ Running Tests

bashpytest tests/ -v

Expected output:

tests/test\_products.py::test\_create\_product        PASSED

tests/test\_sales.py::test\_sale\_success             PASSED

tests/test\_sales.py::test\_sale\_insufficient\_stock  PASSED

tests/test\_sales.py::test\_sale\_product\_not\_found   PASSED

4 passed in \~1s

🔍 Key Features

Layered architecture: models / schemas / crud / routers separation

Input validation: stock and quantity constraints enforced at the schema level

Descriptive HTTP errors: 404 for missing products, 400 for insufficient stock

Automatic stock update: each sale reduces product stock in real time

Automated tests: edge cases covered with unique SKUs per test run

📦 API de Gestión de Inventario

Una API REST construida con FastAPI y SQLAlchemy para gestionar el stock de productos y las ventas de pequeños negocios. Desarrollada como proyecto de portfolio backend con arquitectura limpia, validación de datos y tests automatizados.

🛠️ Tecnologías utilizadas

Python 3.10+

FastAPI — framework web moderno y de alto rendimiento

SQLAlchemy — ORM para gestión de base de datos

PostgreSQL — base de datos relacional hosteada en Railway

Pydantic v2 — validación y serialización de datos

Pytest — testing automatizado

📁 Estructura del proyecto

inventario/

├── app/

│   ├── main.py          # Punto de entrada, registro de routers

│   ├── models.py        # Modelos de base de datos con SQLAlchemy

│   ├── schemas.py       # Schemas Pydantic con validaciones

│   ├── crud.py          # Capa de operaciones con la base de datos

│   ├── database.py      # Conexión y manejo de sesiones

│   └── routers/

│       ├── products.py  # Endpoints de productos

│       └── sales.py     # Endpoints de ventas

└── tests/

├── test\_products.py

└── test\_sales.py

🚀 Cómo correrlo



Clonar el repositorio

bashgit clone https://github.com/Shaco10/inventory-api.git

cd inventory-api

Instalar dependencias

bashpip install fastapi sqlalchemy uvicorn httpx pytest pydantic

Iniciar el servidor

bashuvicorn app.main:app --reload



En Windows con Python de la Microsoft Store, usá: py -m uvicorn app.main:app --reload



Abrir la documentación interactiva

http://127.0.0.1:8000/docs



🔌 Endpoints disponibles

Productos

MétodoEndpointDescripciónPOST/products/Crear un nuevo productoGET/products/Listar todos los productosPUT/products/{id}Actualizar un productoDELETE/products/{id}Eliminar un producto

Ventas

MétodoEndpointDescripciónPOST/sales/Registrar una venta (descuenta stock automáticamente)GET/sales/Listar todas las ventas

✅ Correr los tests

bashpytest tests/ -v

Resultado esperado:

tests/test\_products.py::test\_create\_product        PASSED

tests/test\_sales.py::test\_sale\_success             PASSED

tests/test\_sales.py::test\_sale\_insufficient\_stock  PASSED

tests/test\_sales.py::test\_sale\_product\_not\_found   PASSED

4 passed en \~1s

