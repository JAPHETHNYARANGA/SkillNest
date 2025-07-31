from fastapi import HTTPException, UploadFile
from app.db.session import get_db
from app.schemas.course import CourseCreate, CourseOut
from app.utils.video import process_video_upload
from sqlalchemy.orm import Session

class CourseService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
    
    def create_course(self, course: CourseCreate, instructor_id: int):
        # Implementation here
        pass
    
    def upload_video(self, course_id: int, video: UploadFile, user_id: int):
        # Save and process video
        video_url = process_video_upload(video)
        # Save to database
        return {"message": "Video uploaded successfully", "video_url": video_url}