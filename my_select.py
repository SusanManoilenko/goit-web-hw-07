from sqlalchemy import func, desc
from models import Student, Grade, Course, Teacher, Group

def select_1(session):
    return session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Grade).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()

def select_2(session, course_name):
    return session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Grade).join(Course).filter(Course.name == course_name)\
        .group_by(Student.id).order_by(desc('avg_grade')).first()

# Implement other queries similarly
