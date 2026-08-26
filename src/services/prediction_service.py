import pandas as pd

from src.services.model_loader import load_model
from src.services.feature_validator import validate_student_features

from src.ai_career_report import generate_career_report


def predict_student(student_data):
    """
    Predict placement status and generate AI report.

    Parameters
    ----------
    student_data : dict

    Returns
    -------
    dict
    """

    model = load_model()

    expected_features = model.feature_names_in_

    student_df = pd.DataFrame([student_data])

    student_df = validate_student_features(
        student_df,
        expected_features
    )

    prediction = model.predict(student_df)[0]

    probabilities = model.predict_proba(student_df)[0]

    classes = model.classes_

    prediction_index = list(classes).index(prediction)

    confidence = round(probabilities[prediction_index] * 100, 2)

    report = generate_career_report(
        student_data,
        prediction,
        confidence
    )

    return {

        "prediction": prediction,

        "probability": confidence,

        "report": report,

        "student_profile": student_data

    }