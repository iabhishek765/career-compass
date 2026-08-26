from src.services.prediction_service import predict_student
from src.services.recommendation_engine import generate_recommendations


def process_student(student_data):
    """
    Complete student analysis pipeline.

    Returns:
        dict
    """

    prediction_result = predict_student(student_data)

    recommendations = generate_recommendations(student_data)

    return {
        "prediction": prediction_result["prediction"],
        "probability": prediction_result["probability"],
        "report": prediction_result["report"],
        "recommendations": recommendations
    }