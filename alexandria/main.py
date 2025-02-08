import uvicorn

from alexandria.app.app import create_app
from alexandria.app.settings import Settings


def run_app():
    settings = Settings()
    # aqui se importan los settings
    # tambien se importa la función create_app
    app = create_app(settings)
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    app = run_app()
