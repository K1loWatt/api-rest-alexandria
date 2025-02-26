from sqlalchemy import create_engine
from alexandria.app.settings import Settings
from alexandria.infrastructure.orm import metadata
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    settings = Settings()
    username = os.environ["DB_USER"]
    password = os.environ["DB_PASSWORD"]
    engine = create_engine(settings.db_uri(username, password))
    metadata.create_all(engine)
    print("Tables created successfully.")