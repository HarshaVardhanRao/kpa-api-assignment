# KPA API Assignment

## Tech Stack
- FastAPI (Python)
- PostgreSQL
- SQLAlchemy
- Pydantic
- Docker & Docker Compose
- JWT Auth

## Project Structure
- `main.py`: FastAPI app entrypoint
- `models.py`: SQLAlchemy models
- `schemas.py`: Pydantic models
- `database.py`: DB connection/session
- `crud.py`: DB operations
- `routers/`: API routes
- `config.py` & `.env`: Environment variables

## How to Set Up the Project

### With Docker (Recommended)
1. Copy `.env` and adjust DB credentials if needed.
2. Build and start services:
   ```bash
   docker-compose up --build
   ```
3. Access FastAPI docs at [http://localhost:8000/docs](http://localhost:8000/docs)

### Without Docker (Optional)
1. Install PostgreSQL and Python 3.12+ locally.
2. Create a DB matching `.env`.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run DB migrations (or create tables):
   ```bash
   python3 -c "from database import Base, engine; import models; Base.metadata.create_all(bind=engine)"
   ```
5. Start app:
   ```bash
   uvicorn main:app --reload
   ```

## Key Features Implemented
- **User Authentication:** JWT-based login with `/auth/login` using phone/password.
- **Form Submission:** Authenticated users can submit form data via `/form/submit`.
- **Form Retrieval:** Authenticated users can fetch form data by ID via `/form/{form_id}`.
- **PostgreSQL Persistence:** All data is stored in a PostgreSQL database.
- **OpenAPI Docs:** Interactive API docs available at `/docs`.
- **Dockerized:** Full Docker and Docker Compose support for easy setup.
- **Environment Variables:** All sensitive config is loaded from `.env`.
- **Default User:** On first run, a default user is created (phone: `7760873976`, password: `to_share@123`).
- **User Registration:** New users can register with phone and password via `/auth/register`.
- **Postman Collection:** Provided for quick API testing.

## API Endpoints Implemented
### 1. `POST /auth/login`
- **Request:**
  ```json
  { "phone": "7760873976", "password": "to_share@123" }
  ```
- **Response:**
  ```json
  { "access_token": "<jwt>", "token_type": "bearer" }
  ```

### 1a. `POST /auth/register`
- **Request:**
  ```json
  { "phone": "9999999999", "password": "your_password" }
  ```
- **Response:**
  ```json
  { "id": 2, "phone": "9999999999" }
  ```

### 2. `POST /form/submit` (Auth required)
- **Request:**
  ```json
  { "name": "John Doe", "email": "john@example.com", "phone": "1234567890", "address": "Somewhere" }
  ```
- **Response:**
  ```json
  { "id": 1, "name": "John Doe", "email": "john@example.com", "phone": "1234567890", "address": "Somewhere" }
  ```

### 3. `GET /form/{form_id}` (Auth required)
- **Response:**
  ```json
  { "id": 1, "name": "John Doe", "email": "john@example.com", "phone": "1234567890", "address": "Somewhere" }
  ```

## Authentication
- Use `/auth/login` to get JWT token. Pass as `Authorization: Bearer <token>` for protected endpoints.
- Default user: phone `7760873976`, password `to_share@123` (inserted if not present).

## Environment Variables
- `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `SECRET_KEY`

## Postman Collection
See `postman_collection.json` for ready-to-use requests.

## Limitations & Assumptions
- Only two endpoints from the referenced Swagger doc are implemented for demo purposes.
- No pagination or advanced validation on form fields beyond basic types.
- No email/phone uniqueness validation for form data.
- No production-grade error handling or logging (for demo only).
- Assumes Docker and PostgreSQL are available on the host system.