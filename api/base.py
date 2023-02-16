"""SQL Engine driver"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:password@localhost:5432/')
Session = sessionmaker(bind=engine)

Base = declarative_base()