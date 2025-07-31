from fastapi import APIRouter, Depends, UploadFile, File
from app.schemas.course import CourseCreate, CourseOut
from app.services.course_service import CourseService
from app.core.security import get_current_user

router = APIRouter()

@router.post("/courses/", response_model=CourseOut)
def create_course(
    course: CourseCreate,
    service: CourseService = Depends(),
    current_user=Depends(get_current_user)
):
    return service.create_course(course, current_user.id)

@router.post("/courses/{course_id}/videos/")
def upload_video(
    course_id: int,
    video: UploadFile = File(...),
    service: CourseService = Depends(),
    current_user=Depends(get_current_user)
):
    return service.upload_video(course_id, video, current_user.id)