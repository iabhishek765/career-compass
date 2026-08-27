from src.ai_career_report import generate_career_report


student_data = {
    "CGPA": 8.9,
    "DSA_Level": "Advanced",
    "Projects": 4,
    "Internships": 1,
    "SQL_Level": "Intermediate"
}

prediction = "Placed"

probability = 94.32


report = generate_career_report(
    student_data,
    prediction,
    probability
)

print("=" * 60)
print("CAREER REPORT")
print("=" * 60)
print(report)