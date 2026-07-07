from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DB_USER = "dev"
DB_PASSWORD = "devpassword"
DB_HOST = "localhost"
DB_PORT = 3306
DB_NAME = "py_kardex"


DATABASE_URL = (
    f"mysql+mysqlconnector://"
    f"{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


engine = create_engine(
    DATABASE_URL,
    echo=True, # para ver el SQL en consola
    future=True
)

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)

Base = declarative_base()