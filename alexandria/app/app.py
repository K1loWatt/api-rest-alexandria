import asyncio
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine

from .router import router
from .settings import Settings


def create_life_span_with_settings(settings: Settings):
    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
        engine = await asyncio.to_thread(create_async_engine(settings.db_uri))
        app.state.engine = engine
        yield
        await engine.dispose()

    return lifespan


def create_app(settings: Settings) -> FastAPI:
    lifespan = create_life_span_with_settings(settings)
    app = FastAPI(title=settings.app_name, version=settings.version, lifespan=lifespan)
    app.include_router(router)

    return app
