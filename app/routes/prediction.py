from fastapi import APIRouter

from app.schemas.student import StudentRequest
from app.schemas.response import PredictionResponse

from src.services.student_service import process_student
from repositories.report_repository import ReportRepository

router = APIRouter(
    prefix="/predict",
    tags=["Career Compass Prediction"]
)

@router.post(
    "/",
    response_model=PredictionResponse
)
def predict(student: StudentRequest):

    result = process_student(student.dict())

    report_data = {
        "prediction": result["prediction"],
        "confidence": result["probability"],
        "career_report": result["report"],
        "career_path": result["recommendations"]["career_path"],
        "recommended_courses": result["recommendations"]["recommended_courses"],
        "recommended_projects": result["recommendations"]["recommended_projects"],
        "recommended_certifications": result["recommendations"]["recommended_certifications"],
        "skills_to_improve": result["recommendations"]["missing_skills"],
        "student_answers": student.dict()
    }

    report_id = ReportRepository.save_report(report_data)

    result["report_id"] = report_id

    return result