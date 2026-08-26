"""
Recommendation Engine

Generates career recommendations based on
the student's profile.
"""


def generate_recommendations(student_data):
    """
    Generate rule-based recommendations.

    Parameters
    ----------
    student_data : dict

    Returns
    -------
    dict
    """

    courses = []
    certifications = []
    projects = []
    missing_skills = []
    career_path = []

    # ----------------------------
    # SQL
    # ----------------------------

    sql = student_data.get("SQL_Level", "").lower()

    if sql == "beginner":
        missing_skills.append("SQL")
        courses.append("Advanced SQL for Data Science")

    elif sql == "intermediate":
        missing_skills.append("Advanced SQL")


    # ----------------------------
    # Statistics
    # ----------------------------

    stats = student_data.get("Statistics_Level", "").lower()

    if stats != "advanced":
        missing_skills.append("Statistics & Probability")
        courses.append("Statistics for Machine Learning")

    elif stats == "intermediate":
        missing_skills.append("Advanced Statistics")

# ----------------------------
# Machine Learning
# ----------------------------

    ml = student_data.get("MachineLearning_Level", "").lower()

    if ml == "beginner":
        missing_skills.append("Machine Learning Concepts")
        courses.append("Machine Learning Foundations")

    elif ml == "intermediate":
        missing_skills.append("Advanced Machine Learning Concepts")
        courses.append("Advanced Machine Learning")


# ----------------------------
# Deep Learning
# ----------------------------

    dl = student_data.get("DeepLearning_Level", "").lower()

    if dl != "beginner":
        missing_skills.append("Deep Learning")
        courses.append("Deep Learning Specialization")

    elif dl == "intermediate":
         missing_skills.append("Advanced Deep Learning")
         courses.append("Deep Learning Specialization")

# ----------------------------
# Project Recommendations
# ----------------------------

    role = student_data.get("Target_Role", "").strip().lower()

    ml_projects = int(student_data.get("AI_ML_Projects", 0))
    deployment = student_data.get("Deployment_Experience", "").lower()

    # ---------- AI / ML Engineer ----------

    if role in ["ai/ml engineer", "ml engineer", "machine learning engineer"]:

        if ml_projects == 0:
            projects.extend([
                "Student Performance Prediction",
                "House Price Prediction"
            ])

        elif ml_projects <= 2:
            projects.extend([
                "Customer Churn Prediction",
                "End-to-End ML Pipeline"
            ])

        else:
            projects.extend([
                "MLOps Pipeline",
                "RAG AI Assistant"
            ])

    # ---------- Data Scientist ----------

    elif role == "data scientist":

        if ml_projects == 0:
            projects.extend([
                "Sales Prediction",
                "Customer Segmentation"
            ])

        elif ml_projects <= 2:
            projects.extend([
                "Recommendation System",
                "Fraud Detection"
            ])

        else:
            projects.extend([
                "Time Series Forecasting",
                "Production ML Pipeline"
            ])

    # ---------- Data Analyst ----------

    elif role == "data analyst":

        projects.extend([
            "Sales Dashboard in Power BI",
            "HR Analytics Dashboard"
        ])

    # ---------- Software Engineer ----------

    elif role == "software engineer":

        projects.extend([
            "Task Management API",
            "E-Commerce Backend"
        ])

    # ---------- Default ----------

    else:

        projects.extend([
            "Portfolio Website",
            "Python Automation Tool"
        ])

    # ---------- Deep Learning Bonus ----------

    if dl == "beginner":
        projects.append("MNIST Digit Classifier")

    elif dl == "intermediate":
        projects.append("CNN Image Classifier")

    elif dl == "advanced":
        projects.append("Object Detection using YOLO")

    # ---------- Deployment Bonus ----------

    if deployment == "no":
        projects.append("Deploy ML Model using FastAPI")

    else:
        projects.append("Build & Deploy Complete MLOps Pipeline with Docker & Kubernetes")

    # Remove duplicate recommendations

    projects = list(dict.fromkeys(projects))

    # ----------------------------
    # GitHub
    # ----------------------------

    if student_data.get("GitHub_Profile") == "No":
        missing_skills.append("GitHub Portfolio")


    # ----------------------------
    # Deployment
    # ----------------------------

    if deployment == "no":
        missing_skills.append("Model Deployment")

    # ----------------------------
    # Certifications
    # ----------------------------


    certifications.extend([
        "TensorFlow Developer Certificate",
        "AWS Cloud Practitioner",
        "Microsoft Azure AI Fundamentals"
    ])

       # -------------------------
    # Career Path
    # -------------------------

    role = student_data.get("Target_Role", "").strip().lower()

    if role in ["ai/ml engineer", "ml engineer", "machine learning engineer"]:
        career_path.extend([
            "Build Strong Python, SQL & ML Foundations",
            "Develop End-to-End Machine Learning Projects",
            "Gain Model Deployment & MLOps Experience",
            "Machine Learning / AI Engineer",
            "Senior AI/ML Engineer"
        ])

    elif role == "data scientist":
        career_path.extend([
            "Strengthen Statistics, Python & SQL",
            "Build Data Analysis & Machine Learning Projects",
            "Develop End-to-End Data Science Projects",
            "Data Scientist",
            "Senior Data Scientist"
        ])

    elif role == "data analyst":
        career_path.extend([
            "Strengthen Excel, SQL & Statistics",
            "Learn Data Visualization & BI Tools",
            "Build Data Analytics Projects",
            "Data Analyst",
            "Senior Data Analyst"
        ])

    elif role == "software engineer":
        career_path.extend([
            "Strengthen Programming & DSA Fundamentals",
            "Build Software Development Projects",
            "Learn Backend, APIs & Databases",
            "Software Engineer",
            "Senior Software Engineer"
        ])

    else:
        career_path.extend([
            "Strengthen Core Technical Fundamentals",
            "Build Domain-Specific Projects",
            "Gain Practical Industry Experience",
            "Apply for Entry-Level Technical Roles",
            "Progress Toward Senior Roles"
        ])

    return {

        "recommended_courses": courses,

        "recommended_projects": projects,

        "recommended_certifications": certifications,

        "missing_skills": missing_skills,

        "career_path": career_path
    }