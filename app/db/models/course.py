from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime

class Course(Base):
    __tablename__ = "courses"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    instructor_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    price = Column(Integer)  # in cents
    
    instructor = relationship("User", back_populates="courses_taught")
    students = relationship("User", secondary="enrollments", back_populates="courses_enrolled")
    videos = relationship("CourseVideo", back_populates="course")

class CourseVideo(Base):
    __tablename__ = "course_videos"
    
    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    title = Column(String)
    description = Column(String)
    video_url = Column(String)
    duration = Column(Integer)  # in seconds
    order = Column(Integer)
    
    course = relationship("Course", back_populates="videos")