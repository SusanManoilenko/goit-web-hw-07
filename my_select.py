from sqlalchemy import func, desc
from models import Student, Grade, Course, Teacher, Group

def select_1(session):
    return session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Grade).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()

def select_2(session, course_name):
    return session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Grade).join(Course).filter(Course.name == course_name)\
        .group_by(Student.id).order_by(desc('avg_grade')).first()

def select_3(session, course_name):
    return session.query(Course.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Grade).filter(Course.name == course_name)\
        .group_by(Course.id).order_by(desc('avg_grade')).all()

def select_4(session):
    return session.query(Teacher.fullname, func.count(Course.id).label('courses_count'))\
        .join(Course).group_by(Teacher.id).order_by(desc('courses_count')).all()

def select_5(session, teacher_name):
    return session.query(Course.name)\
        .join(Teacher).filter(Teacher.fullname == teacher_name)\
        .all()

def select_6(session, group_name):
    return session.query(Student.fullname, Group.name)\
        .join(Group).filter(Group.name == group_name)\
        .all()

def select_7(session, group_name, course_name):
    return session.query(Student.fullname, Grade.grade)\
        .join(Group).join(Grade).join(Course)\
        .filter(Group.name == group_name, Course.name == course_name)\
        .all()

def select_8(session, teacher_name):
    return session.query(Course.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Grade).join(Course).join(Teacher)\
        .filter(Teacher.fullname == teacher_name)\
        .group_by(Course.id).order_by(desc('avg_grade')).all()

def select_9(session, student_name):
    return session.query(Student.fullname, Grade.grade, Course.name)\
        .join(Grade).join(Course)\
        .filter(Student.fullname == student_name)\
        .all()

def select_10(session, student_name, teacher_name):
    return session.query(Student.fullname, Course.name, Grade.grade)\
        .join(Grade).join(Course).join(Teacher)\
        .filter(Student.fullname == student_name, Teacher.fullname == teacher_name)\
        .all()

