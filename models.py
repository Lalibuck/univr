from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Faculty(Base):

    __tablename__ = 'Faculty'

    id = Column('id', Integer, primary_key=True)
    address = Column('name', String(255))

    group = relationship('FGroup')
    hr = relationship('HR_record')

    def __int__(self, id, faculty):
        self.id = id
        self.faculty = faculty

    def __repr__(self):
        return self.address

class FGroup(Base):

    __tablename__ = 'FGroup'

    id = Column('id', Integer, primary_key=True)
    faculty_id = Column('faculty_id', Integer, ForeignKey('Faculty.id'), nullable=True)
    faculty = relationship('Faculty', foreign_keys=[faculty_id])

    student = relationship('Student')

    def __int__(self, id, faculty_id):
        self.id = id
        self.faculty_id = faculty_id

    def __repr__(self):
        return '%s'%self.id

class Student(Base):

    __tablename__ = 'Student'

    id = Column('id', Integer, primary_key=True)
    first_name = Column('first_name', String(255))
    last_name = Column('last_name', String(255))
    group_id = Column('group_id', Integer, ForeignKey('FGroup.id'), nullable=True)
    group = relationship('FGroup', uselist=False)
    exam_record = relationship('Exam_record')

    def __int__(self, id, first_name, last_name, group_id):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.group_id = group_id

    def __repr__(self):
        return '%s %s'%\
               (self.first_name, self.last_name)

class Staff(Base):

    __tablename__ = 'Staff'

    id = Column('id', Integer, primary_key=True)
    first_name = Column('first_name', String(255))
    last_name = Column('last_name', String(255))

    exam = relationship('Exam')
    hr = relationship('HR_record')

    def __int__(self, id,  first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return '%s %s'%\
               (self.first_name, self.last_name)

class HR_record(Base):

    __tablename__ = 'HR_record'

    staff_id = Column('staff_id', Integer, ForeignKey('Staff.id'), primary_key=True)
    staff = relationship('Staff', foreign_keys=[staff_id])
    faculty_id = Column('faculty_id', Integer, ForeignKey('Faculty.id'), primary_key=True)
    faculty = relationship('Faculty', foreign_keys=[faculty_id])
    position = Column('position', String(255))

    def __int__(self, staff_id, faculty_id, position):
        self.staff_id = staff_id
        self.faculty_id = faculty_id
        self.position = position

    def __repr__(self):
        return '%s'%\
               (self.position)

class Exam(Base):

    __tablename__ = 'Exam'

    id = Column('id', Integer, primary_key=True)
    discipline = Column('discipline', String(255))
    staff_id = Column('staff_id', Integer, ForeignKey('Staff.id'))
    staff = relationship('Staff', foreign_keys=[staff_id])

    exam_record = relationship('Exam_record')

    def __int__(self, id,  discipline, staff_id):
        self.id = id
        self.discipline = discipline
        self.staff_id = staff_id

    def __repr__(self):
        return '%s'%\
               (self.discipline)

class Exam_record(Base):

    __tablename__ = 'Exam_record'

    student_id = Column('student_id', Integer, ForeignKey('Student.id'), primary_key=True)
    student = relationship('Student', foreign_keys=[student_id])
    exam_id = Column('exam_id', Integer, ForeignKey('Exam.id'), primary_key=True)
    exam = relationship('Exam', foreign_keys=[exam_id])
    grade = Column('grade', String(255))
    date = Column('date', Date)


    def __int__(self, student_id, exam_id, grade, date):
        self.student_id = student_id
        self.exam_id = exam_id
        self.grade = grade
        self.date = date

    def __repr__(self):
        return '%s %s'%\
               (self.grade, self.date)
