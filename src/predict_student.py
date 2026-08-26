import joblib
import pandas as pd
from ai_career_report import generate_career_report


# ------------------------------------------------------------
# 1. Define Model Path
# ------------------------------------------------------------

MODEL_PATH = "models/final_placement_model.joblib"


# ------------------------------------------------------------
# 2. Load Saved Model
# ------------------------------------------------------------

print("\nLoading Career Compass prediction model...")

model = joblib.load(MODEL_PATH)

print("Model loaded successfully!")


# ------------------------------------------------------------
# 3. Display Model Information
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("CAREER COMPASS PREDICTION SYSTEM")
print("=" * 60)

print("\nModel ready to make student placement predictions.")


# ------------------------------------------------------------
# 4. Inspect Expected Model Input Features
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("EXPECTED MODEL INPUT FEATURES")
print("=" * 60)

if hasattr(model, "feature_names_in_"):

    expected_features = model.feature_names_in_

    print(f"\nTotal Expected Features: {len(expected_features)}")

    print("\nFeature Names:")

    for feature_number, feature_name in enumerate(
        expected_features,
        start=1
    ):
        print(f"{feature_number}. {feature_name}")

else:

    print(
        "\nFeature names are not available "
        "inside the saved model."
    )


    # ------------------------------------------------------------
# 5. Create Sample Student Data
# ------------------------------------------------------------

sample_student = {
    "Age": 22,
    "Gender": "Male",
    "Branch": "AI/ML",
    "Graduation_Year": 2027,
    "CGPA": 8.5,
    "LeetCode_Problems": 350,
    "DSA_Level": "Advanced",
    "GitHub_Repositories": 8,
    "Open_Source_Contribution": "Yes",
    "Total_Projects": 5,
    "Major_Project_Level": "Advanced",
    "AI_ML_Projects": 3,
    "Deployment_Experience": "Yes",
    "Internship_Count": 2,
    "Internship_Domain": "AI/ML",
    "Python_Level": "Advanced",
    "SQL_Level": "Intermediate",
    "PowerBI_Level": "Intermediate",
    "MachineLearning_Level": "Advanced",
    "Statistics_Level": "Intermediate",
    "DeepLearning_Level": "Intermediate",
    "LinkedIn_Profile": "Yes",
    "GitHub_Profile": "Yes",
    "Portfolio_Website": "Yes",
    "Industry_Certifications": 3,
    "Communication_Level": "Advanced",
    "Target_Role": "ML Engineer",
    "Preferred_Domain": "AI/ML"
}


# ------------------------------------------------------------
# 6. Convert Sample Student to DataFrame
# ------------------------------------------------------------

sample_student_df = pd.DataFrame([sample_student])


# ------------------------------------------------------------
# 7. Display Sample Student
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("SAMPLE STUDENT PROFILE")
print("=" * 60)

print(
    sample_student_df
    .T
    .to_string(header=False)
)

print("\nSample student data created successfully!")

# ------------------------------------------------------------
# Validate Input Features
# ------------------------------------------------------------

expected_feature_set = set(expected_features)
input_feature_set = set(sample_student_df.columns)

missing_features = expected_feature_set - input_feature_set
extra_features = input_feature_set - expected_feature_set

if missing_features:
    raise ValueError(
        f"Missing required features: {sorted(missing_features)}"
    )

if extra_features:
    raise ValueError(
        f"Unexpected extra features: {sorted(extra_features)}"
    )

# Ensure exact feature order expected by the model
sample_student_df = sample_student_df[list(expected_features)]

print("\nStudent input features validated successfully!")

# ------------------------------------------------------------
# 8. Make Placement Prediction
# ------------------------------------------------------------

prediction = model.predict(sample_student_df)

predicted_status = prediction[0]


# ------------------------------------------------------------
# 9. Display Prediction Result
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("PLACEMENT PREDICTION RESULT")
print("=" * 60)

print(f"\nPredicted Placement Status: {predicted_status}")

print("\nPrediction completed successfully!")

# ------------------------------------------------------------
# 10. Calculate Prediction Probabilities
# ------------------------------------------------------------

prediction_probabilities = model.predict_proba(sample_student_df)

class_labels = model.classes_

student_probabilities = prediction_probabilities[0]


# ------------------------------------------------------------
# 11. Display Prediction Probabilities
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("PLACEMENT PROBABILITY ANALYSIS")
print("=" * 60)

for class_label, probability in zip(
    class_labels,
    student_probabilities
):
    print(
        f"{class_label} Probability: "
        f"{probability * 100:.2f}%"
    )

    # ------------------------------------------------------------
# 12. Get Probability of Predicted Class
# ------------------------------------------------------------

predicted_class_index = list(class_labels).index(predicted_status)

predicted_probability = student_probabilities[predicted_class_index]


# ------------------------------------------------------------
# 13. Display Final Prediction Summary
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("CAREER COMPASS - FINAL PREDICTION SUMMARY")
print("=" * 60)

print(f"\nPrediction: {predicted_status}")

print(
    f"Model-Estimated Probability: "
    f"{predicted_probability * 100:.2f}%"
)

# ------------------------------------------------------------
# 14. Generate AI Career Report
# ------------------------------------------------------------

print("\nGenerating personalized AI career report...")

career_report = generate_career_report(
    student_data=sample_student,
    prediction=str(predicted_status),
    probability=predicted_probability * 100
)

print("Career report generated successfully!")

# ------------------------------------------------------------
# 15. Display AI Career Report
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("AI CAREER REPORT")
print("=" * 60)

print()

print(career_report)

print("\n" + "=" * 60)

print("\n" + "=" * 60)