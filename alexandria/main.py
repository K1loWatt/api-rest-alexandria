import uvicorn

from alexandria.app.app import create_app
from alexandria.app.settings import Settings


def run_app():
    settings = Settings()
    app = create_app(settings)
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    app = run_app()
