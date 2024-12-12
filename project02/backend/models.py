from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from db import Base


class Instructor(Base):
    __tablename__ = "instructors"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    full_name = Column(String, nullable=False, unique=True)
    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)

    courses = relationship(
        "Course", secondary="course_instructors", back_populates="instructors"
    )


class CourseInstructor(Base):
    __tablename__ = "course_instructors"
    course_id = Column(Integer, ForeignKey("courses.crn"), primary_key=True)
    instructor_id = Column(Integer, ForeignKey("instructors.id"), primary_key=True)


class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True)
    full_location = Column(String, nullable=False, unique=True)
    building = Column(String, nullable=True)
    room = Column(String, nullable=True)

    courses = relationship("Course", back_populates="location")


class Course(Base):
    __tablename__ = "courses"
    crn = Column(Integer, primary_key=True)
    department = Column(String, nullable=False)
    title = Column(String, nullable=False)

    # Relationships
    instructors = relationship(
        "Instructor", secondary="course_instructors", back_populates="courses"
    )
    location_id = Column(Integer, ForeignKey("locations.id"), nullable=True)
    location = relationship("Location", back_populates="courses")


class ScheduleCourse(Base):
    __tablename__ = "schedule_courses"
    course_crn = Column(Integer, ForeignKey("courses.crn"), primary_key=True)
    schedule_id = Column(Integer, ForeignKey("schedules.id"), primary_key=True)


class Schedule(Base):
    __tablename__ = "schedules"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    user = relationship("User", back_populates="schedules")

    courses = relationship(
        "Course", secondary="schedule_courses", back_populates="schedules"
    )


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)

    # Relationship
    schedules = relationship("Schedule", back_populates="user")


Base = declarative_base()
