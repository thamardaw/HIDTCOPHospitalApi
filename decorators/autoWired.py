from sqlalchemy.orm import Session
from fastapi import Depends
from schemas.token import TokenData
from utils.oauth2 import extract_token_data
from infrastructure.session import get_db

def autoWired(dependencies:dict={}):
    def service_decorator(service):
        def wrapped_service(db:Session=Depends(get_db),tokenData:TokenData=Depends(extract_token_data)):
            modf_service = service()
            for key,repo in dependencies.items():
                setattr(modf_service,key,repo(db,tokenData))
            return modf_service
        return wrapped_service
    return service_decorator