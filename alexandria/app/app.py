from fastapi import FastAPI
from contextlib import asynccontextmanager
from .router import router

from .settings import Settings
from typing import AsyncGenerator

#async def db_engine_creation():
#    return #engine

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    
    #aqui todo lo que va antes de la inicialización de la propia aplicaci'on
    #aqui va la inicialización de la BBDD y se agrega al app.state
    print("Starting up...")
    yield
    #aqui va el engine dispose
    print("Shutting down...")
    
    #funcion para el lifespan
    #TODO entender diferencia entre async def con y sin asynccontextmanager

def create_app(settings: Settings) -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        description=settings['app_description'],
        version=settings.version,
        openapi_tags=settings['tags'],
        life_span=lifespan
    )

    app.include_router(router)

    return app