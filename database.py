from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker, declarative_base
Base=declarative_base()
load_dotenv()
import os 
from sqlalchemy import create_engine
usuario=os.getenv('DB_USER')
contraseña=os.getenv('DB_PASSWORD')
host=os.getenv('DB_HOST')
port=os.getenv('DB_PORT')
wines=os.getenv('DB_NAME')
DATABASE_URL=f"postgresql+psycopg2://{usuario}:{contraseña}@{host}:{port}/{wines}"
engine = create_engine(DATABASE_URL)
print(DATABASE_URL)
SessionLocal= sessionmaker(autocommit=False, autoflush=False, bind=engine)
session=SessionLocal()
Base.metadata.create_all(bind=engine)
