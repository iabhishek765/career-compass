def analyze_student(student_data):
    """
    Analyze the student's profile and identify strengths
    and improvement areas for AI-generated career guidance.
    """

    strengths = []
    improvements = []

    # ----------------------------------------------------
    # Academic Performance
    # ----------------------------------------------------

    cgpa = student_data.get("CGPA", 0)

    if cgpa >= 8.5:
        strengths.append("Excellent academic performance")
    elif cgpa >= 7.5:
        strengths.append("Good academic record")
    else:
        improvements.append("Improve academic performance")

    # ----------------------------------------------------
    # DSA
    # ----------------------------------------------------

    dsa = student_data.get("DSA_Level", "").lower()

    if dsa == "advanced":
        strengths.append("Strong Data Structures and Algorithms skills")
    elif dsa == "intermediate":
        strengths.append("Good DSA foundation")
    else:
        improvements.append("Strengthen Data Structures and Algorithms")

    # ----------------------------------------------------
    # Python
    # ----------------------------------------------------

    python_level = student_data.get("Python_Level", "").lower()

    if python_level == "advanced":
        strengths.append("Strong Python programming skills")
    elif python_level == "intermediate":
        strengths.append("Good Python programming knowledge")
    else:
        improvements.append("Improve Python programming skills")

    # ----------------------------------------------------
    # Machine Learning
    # ----------------------------------------------------

    ml = student_data.get("MachineLearning_Level", "").lower()

    if ml == "advanced":
        strengths.append("Strong Machine Learning knowledge")
    elif ml == "intermediate":
        strengths.append("Good Machine Learning foundation")
    else:
        improvements.append("Improve Machine Learning concepts")

    # ----------------------------------------------------
    # Projects
    # ----------------------------------------------------

    projects = student_data.get("Total_Projects", 0)

    if projects >= 5:
        strengths.append("Excellent project portfolio")
    elif projects >= 3:
        strengths.append("Strong project portfolio")
    elif projects >= 1:
        strengths.append("Practical project experience")
    else:
        improvements.append("Build more real-world projects")

    # ----------------------------------------------------
    # AI/ML Projects
    # ----------------------------------------------------

    ai_projects = student_data.get("AI_ML_Projects", 0)

    if ai_projects >= 2:
        strengths.append("Hands-on AI/ML project experience")
    else:
        improvements.append("Build more AI/ML projects")

    # ----------------------------------------------------
    # Internship
    # ----------------------------------------------------

    internships = student_data.get("Internship_Count", 0)

    if internships >= 2:
        strengths.append("Strong industry exposure")
    elif internships >= 1:
        strengths.append("Industry internship experience")
    else:
        improvements.append("Gain internship experience")

    # ----------------------------------------------------
    # SQL
    # ----------------------------------------------------

    sql = student_data.get("SQL_Level", "").lower()

    if sql == "advanced":
        strengths.append("Strong SQL skills")
    elif sql == "intermediate":
        strengths.append("Good SQL knowledge")
    else:
        improvements.append("Improve SQL skills")

    # ----------------------------------------------------
    # GitHub
    # ----------------------------------------------------

    github = student_data.get("GitHub_Profile", "No")

    if github == "Yes":
        strengths.append("Maintains an active GitHub profile")
    else:
        improvements.append("Create and maintain a GitHub profile")

    # ----------------------------------------------------
    # Portfolio
    # ----------------------------------------------------

    portfolio = student_data.get("Portfolio_Website", "No")

    if portfolio == "Yes":
        strengths.append("Has a professional portfolio website")
    else:
        improvements.append("Build a personal portfolio website")

    # ----------------------------------------------------
    # Certifications
    # ----------------------------------------------------

    certs = student_data.get("Industry_Certifications", 0)

    if certs >= 3:
        strengths.append("Strong professional certifications")
    elif certs == 0:
        improvements.append("Earn industry-recognized certifications")

    return {
        "strengths": strengths,
        "improvements": improvements
    }