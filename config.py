from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    DB_HOST: str = os.getenv('DB_HOST', 'localhost')
    DB_PORT: str = os.getenv('DB_PORT', '5432')
    DB_NAME: str = os.getenv('DB_NAME', 'kpa_db')
    DB_USER: str = os.getenv('DB_USER', 'postgres')
    DB_PASSWORD: str = os.getenv('DB_PASSWORD', 'postgres')
    SECRET_KEY: str = os.getenv('SECRET_KEY', 'supersecret')

settings = Settings()
