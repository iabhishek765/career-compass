import pandas as pd

from services.model_loader import load_model
from services.feature_validator import validate_student_features


model = load_model()

expected_features = model.feature_names_in_

student = {}

for feature in expected_features:
    student[feature] = 0

student_df = pd.DataFrame([student])

validated = validate_student_features(
    student_df,
    expected_features
)

print("=" * 60)
print("FEATURE VALIDATOR TEST")
print("=" * 60)

print(validated.columns.tolist())

print("\nValidation successful.")