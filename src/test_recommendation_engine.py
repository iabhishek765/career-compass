from services.recommendation_engine import generate_recommendations


student = {
    "SQL_Level": "Intermediate",
    "Statistics_Level": "Intermediate",
    "MachineLearning_Level": "Advanced",
    "DeepLearning_Level": "Intermediate",
    "GitHub_Profile": "Yes",
    "Target_Role": "ML Engineer"
}


recommendations = generate_recommendations(student)

print("=" * 60)
print("RECOMMENDATION ENGINE TEST")
print("=" * 60)

for key, value in recommendations.items():
    print(f"\n{key.upper()}")

    if isinstance(value, list):
        for item in value:
            print(f"- {item}")
    else:
        print(value)