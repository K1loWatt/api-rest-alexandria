from pydantic import BaseSettings


class Settings(BaseSettings):
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "myapp"
    app_name: str = "MyApp"
    debug: bool = False
    version: str = "1.0.0"

    class Config:
        env_file = ".env"

    def db_uri(self, username: str, password: str) -> str:
        return (
            f"postgresql://{username}:{password}@"
            f"{self.db_host}:{self.db_port}/"
            f"{self.db_name}"
        )
