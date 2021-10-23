from fastapi import FastAPI
from db.base import Base
from db.session import engine
from core.config import settings 
from apis.base import router
import uvicorn

def include_router(app):
    app.include_router(router)

def create_tables():          
    Base.metadata.create_all(bind=engine)

def start_application():
	app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
	include_router(app)
	create_tables()    
	return app

app = start_application()

if __name__=='__main__':
	uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True, log_level='info')