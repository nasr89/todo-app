from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.model.sql_model import Base  # Use the full path

db_user: str = "postgres"
db_port: int = 5432
db_host: str = "localhost"
db_password: str = "1142131"

uri: str = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/todo_app"

engine = create_engine(uri)
Base.metadata.create_all(bind=engine)

# session
session = sessionmaker(bind=engine, autoflush=True)

db_session = session()

try:
    connection = engine.connect()
    connection.close()
    print("ping, connected")
except Exception as e:
    print(f"Error: {str(e)}")
