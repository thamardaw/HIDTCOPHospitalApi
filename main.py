from fastapi import FastAPI
from db.base import Base
from db.session import engine
from core.config import settings


def include_router(app):
    pass

def create_tables():          
    print("CREATE TABLE")
    Base.metadata.create_all(bind=engine)

def start_application():
	app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
	include_router(app)
	create_tables()    
	return app

app = start_application()