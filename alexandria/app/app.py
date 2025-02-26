from contextlib import asynccontextmanager
from typing import AsyncGenerator
import asyncio
from fastapi import FastAPI

from .router import router
from .settings import Settings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine


def create_life_span_with_settings(
    settings: Settings
    ):
    
    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:        
        engine = await asyncio.to_thread(create_async_engine(settings.db_uri))
        app.state.engine = engine
        yield
        await engine.dispose()

    return lifespan

def create_app(settings: Settings) -> FastAPI:
    
    lifespan = create_life_span_with_settings(settings)
    app = FastAPI(
        title=settings.app_name, 
        version=settings.version, 
        lifespan=lifespan
        )
    app.include_router(router)

    return app
