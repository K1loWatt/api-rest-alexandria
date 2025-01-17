from pydantic import BaseSettings


class Settings(BaseSettings):

    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "myapp"
    app_name: str = "MyApp"
    debug: bool = False
    version: str = "1.0.0" #TODO get this version from pyproject.toml

    class Config:
        env_file = ".env"     

    @property
    def db_uri(self, username: str, password: str) -> str:
        return (
            f"postgresql+asyncpg://{username}:"
            f"{password}@{self.db_domain}:{self.db_port}"
            f"/{self.db_name}"
        )

