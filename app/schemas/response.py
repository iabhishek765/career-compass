from typing import Dict, List

from pydantic import BaseModel


class RecommendationResponse(BaseModel):
    recommended_courses: List[str]
    recommended_projects: List[str]
    recommended_certifications: List[str]
    missing_skills: List[str]
    career_path: List[str]


class PredictionResponse(BaseModel):

    report_id: int | None = None
    prediction: str
    probability: float
    report: str
    recommendations: RecommendationResponse