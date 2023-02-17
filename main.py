from sqlalchemy import create_engine, Column, Integer, String, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


base = declarative_base()
engine = create_engine('mysql://rashid:R@shid.254@0.0.0.0/my_db')
base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session

