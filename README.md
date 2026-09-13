# PyMart

An online store built with **FastAPI** and **Jinja2** — fully Python-powered.

## Features

- JWT Authentication
- Product & Category Management
- Shopping Cart
- Orders & Payment Simulation
- Admin Panel
- HTML pages with Jinja2 + HTMX (no JavaScript coding required)
- Auto-generated API docs (Swagger)

## Tech Stack

- Python 3.12
- FastAPI
- SQLAlchemy + Alembic
- Jinja2
- SQLite (dev) / PostgreSQL (prod)
- pytest
- Docker

## Installation & Run

git clone https://github.com/Amu-Mehdi/PyMart.git
cd PyMart
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload

Then open: http://localhost:8000/docs

## Project Structure

pymart/
|-- app/
|   |-- core/          # shared config (settings, db, security)
|   |-- models/        # SQLAlchemy models
|   |-- schemas/       # Pydantic schemas
|   |-- repositories/  # data access layer
|   |-- services/      # business logic
|   |-- api/           # JSON API endpoints
|   |-- web/           # HTML pages (Jinja2)
|   |-- templates/     # Jinja2 templates
|   -- static/        # CSS, images, uploads
|-- alembic/           # database migrations
|-- tests/             # pytest tests
-- scripts/           # helper scripts

## License

MIT
