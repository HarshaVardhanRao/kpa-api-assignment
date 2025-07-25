FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv pydantic python-jose[cryptography] passlib[bcrypt]

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
