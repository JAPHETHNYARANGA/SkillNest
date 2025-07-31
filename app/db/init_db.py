from app.db.session import engine, Base
from app.db.models.user import User
from app.db.models.course import Course, CourseVideo

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()