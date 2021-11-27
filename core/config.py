import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

class Settings:
    #APP
    PROJECT_NAME : str = "HIDTCOP"
    PROJECT_VERSION : str = "1.0.0"

    #DB
    #if your username password contains special characters, you will have to use URI escapes.
    POSTGRES_USER : str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD") 
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER","localhost")
    POSTGRES_PORT : str = os.getenv("POSTGRES_PORT",5432)
    POSTGRES_DB : str = os.getenv("POSTGRES_DB","tdd")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    # DATABASE_URL = os.getenv("DATABASE_URL") # heroku postgres comes with one line database url
    # if DATABASE_URL.startswith("postgres://"): # sqlalchemy does not support heroku postgres 
    #     DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
    
    #This is for zmm's problematic password -_-
    DATABASE_URL_ALEMBIC =  f"postgresql://{POSTGRES_USER}:%{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    # DATABASE_URL_ALEMBIC = os.getenv("DATABASE_URL") # heroku postgres comes with one line database url
    # if DATABASE_URL_ALEMBIC.startswith("postgres://"): # sqlalchemy does not support heroku postgres 
    #     DATABASE_URL_ALEMBIC = DATABASE_URL_ALEMBIC.replace("postgres://", "postgresql://", 1)

    #JWT
    SECRET_KEY : str = os.getenv("SECRET_KEY")
    ALGORITHM : str = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = 60
    REFRESH_TOKEN_EXPIRE_MINUTES = 360


settings = Settings()