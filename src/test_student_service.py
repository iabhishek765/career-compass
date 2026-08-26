from src.services.student_service import process_student


student = {
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

result = process_student(student)

print("=" * 70)
print("STUDENT SERVICE TEST")
print("=" * 70)

print("\nPrediction:")
print(result["prediction"])

print("\nProbability:")
print(f"{result['probability']:.2f}%")

print("\nAI Report:")
print(result["report"])

print("\nRecommendations:")
for key, value in result["recommendations"].items():
    print(f"\n{key.upper()}")

    if isinstance(value, list):
        for item in value:
            print("-", item)
    else:
        print(value)