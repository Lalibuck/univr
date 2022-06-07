from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy import create_engine
from models import *

DB_NAME = 'univr.db'

engine = create_engine('sqlite:///%s'%DB_NAME, echo=False)

if os.path.isfile(DB_NAME):
    Session = sessionmaker(bind=engine)
    session = Session()
else:
    Base.metadata.create_all(engine)

