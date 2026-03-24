import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# v2 - precio_venta support
SQLALCHEMY_DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql://postgres:qQwJArobpvmbdNnvPhedFUUaHeRKomHm@postgres.railway.internal:5432/railway"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()