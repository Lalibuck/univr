from sqlalchemy.orm import sessionmaker
from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///univr.db')
Session = sessionmaker(bind=engine)
session = Session()

print(session.query(Student).join(Exam_record).all())
print(session.query(Exam_record).join(Exam).filter(Exam.discipline.like('Math')).all())
print(session.query(Exam_record).join(Exam).join(Staff).filter(Staff.last_name.like('Gavrilova')).all())

