from src.services.prediction_service import predict_student


student = {

    "Age":22,
    "Gender":"Male",
    "Branch":"AI/ML",
    "Graduation_Year":2027,
    "CGPA":8.5,
    "LeetCode_Problems":350,
    "DSA_Level":"Advanced",
    "GitHub_Repositories":8,
    "Open_Source_Contribution":"Yes",
    "Total_Projects":5,
    "Major_Project_Level":"Advanced",
    "AI_ML_Projects":3,
    "Deployment_Experience":"Yes",
    "Internship_Count":2,
    "Internship_Domain":"AI/ML",
    "Python_Level":"Advanced",
    "SQL_Level":"Intermediate",
    "PowerBI_Level":"Intermediate",
    "MachineLearning_Level":"Advanced",
    "Statistics_Level":"Intermediate",
    "DeepLearning_Level":"Intermediate",
    "LinkedIn_Profile":"Yes",
    "GitHub_Profile":"Yes",
    "Portfolio_Website":"Yes",
    "Industry_Certifications":3,
    "Communication_Level":"Advanced",
    "Target_Role":"ML Engineer",
    "Preferred_Domain":"AI/ML"

}

result = predict_student(student)

print("=" * 60)
print("PREDICTION SERVICE TEST")
print("=" * 60)

print(result["prediction"])
print(f"{result['probability']:.2f}%")
print()
print(result["report"])