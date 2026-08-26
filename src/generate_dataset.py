import pandas as pd
import numpy as np
import random

# Set random seeds for reproducibility
np.random.seed(42)
random.seed(42)

# Number of student records
NUM_STUDENTS = 5000

# Generate unique student IDs
student_ids = np.arange(1001, 1001 + NUM_STUDENTS)

print("Dataset generation started...")
print(f"Total students: {NUM_STUDENTS}")
print(f"First Student ID: {student_ids[0]}")
print(f"Last Student ID: {student_ids[-1]}")


# --------------------------------------------------
# Generate Academic Information
# --------------------------------------------------

# Generate student ages between 20 and 24
ages = np.random.randint(20, 25, NUM_STUDENTS)

# Generate gender
genders = np.random.choice(
    ["Male", "Female"],
    size=NUM_STUDENTS,
    p=[0.55, 0.45]
)

# Generate academic branches
branches = np.random.choice(
    ["CSE", "AI/ML", "Data Science", "IT", "ECE"],
    size=NUM_STUDENTS,
    p=[0.30, 0.25, 0.15, 0.20, 0.10]
)

# Generate graduation years
graduation_years = np.random.choice(
    [2025, 2026, 2027, 2028],
    size=NUM_STUDENTS
)

# Generate realistic CGPA values
cgpa = np.random.normal(
    loc=7.5,
    scale=1.0,
    size=NUM_STUDENTS
)

# Keep CGPA values between 5.0 and 10.0
cgpa = np.clip(cgpa, 5.0, 10.0)

# Round CGPA to 2 decimal places
cgpa = np.round(cgpa, 2)


# Create initial DataFrame
df = pd.DataFrame({
    "Student_ID": student_ids,
    "Age": ages,
    "Gender": genders,
    "Branch": branches,
    "Graduation_Year": graduation_years,
    "CGPA": cgpa
})


# Display dataset information
print("\nAcademic information generated successfully!")

print("\nFirst 5 Records:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

# --------------------------------------------------
# Generate Coding Profile
# --------------------------------------------------

# Generate LeetCode problems solved
leetcode_problems = np.random.gamma(
    shape=2.0,
    scale=80,
    size=NUM_STUDENTS
)

# Keep values between 0 and 1000
leetcode_problems = np.clip(
    leetcode_problems,
    0,
    1000
).astype(int)


# Assign DSA level based on LeetCode problems solved
dsa_level = np.select(
    [
        leetcode_problems < 100,
        (leetcode_problems >= 100) & (leetcode_problems < 300),
        leetcode_problems >= 300
    ],
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ],
    default="Beginner"
)


# Generate number of GitHub repositories
github_repositories = np.random.poisson(
    lam=6,
    size=NUM_STUDENTS
)

# Keep repositories between 0 and 30
github_repositories = np.clip(
    github_repositories,
    0,
    30
)


# Generate open-source contribution status
open_source_contribution = np.random.choice(
    ["Yes", "No"],
    size=NUM_STUDENTS,
    p=[0.20, 0.80]
)


# Add coding features to DataFrame
df["LeetCode_Problems"] = leetcode_problems
df["DSA_Level"] = dsa_level
df["GitHub_Repositories"] = github_repositories
df["Open_Source_Contribution"] = open_source_contribution


# Display coding profile information
print("\nCoding profile generated successfully!")

print("\nFirst 5 Records:")
print(
    df[
        [
            "Student_ID",
            "LeetCode_Problems",
            "DSA_Level",
            "GitHub_Repositories",
            "Open_Source_Contribution"
        ]
    ].head()
)

print("\nDSA Level Distribution:")
print(df["DSA_Level"].value_counts())

print("\nUpdated Dataset Shape:")
print(df.shape)


# --------------------------------------------------
# Generate Project Experience
# --------------------------------------------------

# Generate total number of projects
total_projects = np.random.poisson(
    lam=3,
    size=NUM_STUDENTS
)

# Keep total projects between 0 and 10
total_projects = np.clip(
    total_projects,
    0,
    10
)


# Assign major project level based on total projects
major_project_level = np.select(
    [
        total_projects <= 1,
        (total_projects >= 2) & (total_projects <= 4),
        total_projects >= 5
    ],
    [
        "Basic",
        "Intermediate",
        "Advanced"
    ],
    default="Basic"
)


# Generate number of AI/ML projects
ai_ml_projects = np.array([
    np.random.randint(0, project_count + 1)
    for project_count in total_projects
])


# Generate deployment experience
# Students with more projects have a higher chance
# of having deployment experience

deployment_probability = np.clip(
    0.10 + (total_projects * 0.10),
    0.10,
    0.90
)

deployment_experience = np.array([
    np.random.choice(
        ["Yes", "No"],
        p=[probability, 1 - probability]
    )
    for probability in deployment_probability
])


# Add project features to DataFrame
df["Total_Projects"] = total_projects
df["Major_Project_Level"] = major_project_level
df["AI_ML_Projects"] = ai_ml_projects
df["Deployment_Experience"] = deployment_experience


# Display project experience information
print("\nProject experience generated successfully!")

print("\nFirst 5 Project Records:")
print(
    df[
        [
            "Student_ID",
            "Total_Projects",
            "Major_Project_Level",
            "AI_ML_Projects",
            "Deployment_Experience"
        ]
    ].head()
)


print("\nMajor Project Level Distribution:")
print(df["Major_Project_Level"].value_counts())


print("\nDeployment Experience Distribution:")
print(df["Deployment_Experience"].value_counts())


print("\nUpdated Dataset Shape:")
print(df.shape)



# --------------------------------------------------
# Generate Internship Experience
# --------------------------------------------------

# Generate number of internships
internship_count = np.random.choice(
    [0, 1, 2, 3],
    size=NUM_STUDENTS,
    p=[0.35, 0.40, 0.20, 0.05]
)


# Available internship domains
internship_domains = [
    "AI/ML",
    "Data Science",
    "Data Analytics",
    "Web Development",
    "Cloud",
    "Cybersecurity",
    "Other"

]


# Generate internship domain
internship_domain = np.array([
    "None"
    if count == 0
    else np.random.choice(internship_domains)
    for count in internship_count
])


# Add internship features to DataFrame
df["Internship_Count"] = internship_count
df["Internship_Domain"] = internship_domain


# Display internship information
print("\nInternship experience generated successfully!")


print("\nFirst 5 Internship Records:")
print(
    df[
        [
            "Student_ID",
            "Internship_Count",
            "Internship_Domain"
        ]
    ].head()
)


print("\nInternship Count Distribution:")
print(df["Internship_Count"].value_counts())


print("\nInternship Domain Distribution:")
print(df["Internship_Domain"].value_counts())


print("\nUpdated Dataset Shape:")
print(df.shape)



# --------------------------------------------------
# Generate Technical Skills
# --------------------------------------------------

# Skill proficiency levels
skill_levels = [
    "None",
    "Beginner",
    "Intermediate",
    "Advanced"
]


# Generate Python proficiency
python_level = np.random.choice(
    skill_levels,
    size=NUM_STUDENTS,
    p=[0.05, 0.25, 0.50, 0.20]
)


# Generate SQL proficiency
sql_level = np.random.choice(
    skill_levels,
    size=NUM_STUDENTS,
    p=[0.15, 0.35, 0.40, 0.10]
)


# Generate Power BI proficiency
powerbi_level = np.random.choice(
    skill_levels,
    size=NUM_STUDENTS,
    p=[0.35, 0.30, 0.25, 0.10]
)


# Generate Machine Learning proficiency
machine_learning_level = np.random.choice(
    skill_levels,
    size=NUM_STUDENTS,
    p=[0.20, 0.35, 0.35, 0.10]
)


# Generate Statistics proficiency
statistics_level = np.random.choice(
    skill_levels,
    size=NUM_STUDENTS,
    p=[0.10, 0.35, 0.45, 0.10]
)


# Generate Excel proficiency
deeplearning_level = np.random.choice(
    skill_levels,
    size=NUM_STUDENTS,
    p=[0.10, 0.30, 0.45, 0.15]
)


# Add technical skill features to DataFrame
df["Python_Level"] = python_level
df["SQL_Level"] = sql_level
df["PowerBI_Level"] = powerbi_level
df["MachineLearning_Level"] = machine_learning_level
df["Statistics_Level"] = statistics_level
df["DeepLearning_Level"] = deeplearning_level


# Display technical skill information
print("\nTechnical skills generated successfully!")


print("\nFirst 5 Technical Skill Records:")

print(
    df[
        [
            "Student_ID",
            "Python_Level",
            "SQL_Level",
            "PowerBI_Level",
            "MachineLearning_Level",
            "Statistics_Level",
            "DeepLearning_Level"
        ]
    ].head()
)


print("\nPython Level Distribution:")
print(df["Python_Level"].value_counts())


print("\nSQL Level Distribution:")
print(df["SQL_Level"].value_counts())


print("\nUpdated Dataset Shape:")
print(df.shape)



# --------------------------------------------------
# Generate Professional Presence Features
# --------------------------------------------------

# LinkedIn profile availability
linkedin_profile = np.random.choice(
    ["Yes", "No"],
    size=NUM_STUDENTS,
    p=[0.80, 0.20]
)


# GitHub profile based on number of repositories
github_profile = np.where(
    github_repositories > 0,
    "Yes",
    "No"
)


# Portfolio probability based on total projects
portfolio_probability = np.clip(
    0.10 + (total_projects * 0.08),
    0.10,
    0.80
)


# Generate portfolio website availability
portfolio_website = np.array([
    np.random.choice(
        ["Yes", "No"],
        p=[probability, 1 - probability]
    )
    for probability in portfolio_probability
])


# Add professional presence features to DataFrame
df["LinkedIn_Profile"] = linkedin_profile
df["GitHub_Profile"] = github_profile
df["Portfolio_Website"] = portfolio_website


# Display professional presence information
print("\nProfessional presence features generated successfully!")


print("\nFirst 5 Professional Presence Records:")

print(
    df[
        [
            "Student_ID",
            "LinkedIn_Profile",
            "GitHub_Profile",
            "Portfolio_Website"
        ]
    ].head()
)


print("\nLinkedIn Profile Distribution:")
print(df["LinkedIn_Profile"].value_counts())


print("\nGitHub Profile Distribution:")
print(df["GitHub_Profile"].value_counts())


print("\nPortfolio Website Distribution:")
print(df["Portfolio_Website"].value_counts())


print("\nUpdated Dataset Shape:")
print(df.shape)



# --------------------------------------------------
# Generate Industry Certification Feature
# --------------------------------------------------

# Generate number of industry certifications
industry_certifications = np.random.choice(
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    size=NUM_STUDENTS,
    p=[
        0.15,
        0.20,
        0.20,
        0.15,
        0.10,
        0.08,
        0.06,
        0.04,
        0.02
    ]
)


# Add certification feature to DataFrame
df["Industry_Certifications"] = industry_certifications


# Display certification information
print("\nIndustry certification feature generated successfully!")


print("\nFirst 5 Certification Records:")

print(
    df[
        [
            "Student_ID",
            "Industry_Certifications"
        ]
    ].head()
)


print("\nIndustry Certification Distribution:")
print(df["Industry_Certifications"].value_counts().sort_index())


print("\nUpdated Dataset Shape:")
print(df.shape)


# --------------------------------------------------
# Generate Communication Skill Feature
# --------------------------------------------------

# Generate communication skill levels
communication_level = np.random.choice(
    [
        "Poor",
        "Average",
        "Good",
        "Excellent"
    ],
    size=NUM_STUDENTS,
    p=[
        0.10,
        0.35,
        0.40,
        0.15
    ]
)


# Add communication skill feature to DataFrame
df["Communication_Level"] = communication_level


# Display communication skill information
print("\nCommunication skill feature generated successfully!")


print("\nFirst 5 Communication Skill Records:")

print(
    df[
        [
            "Student_ID",
            "Communication_Level"
        ]
    ].head()
)


print("\nCommunication Level Distribution:")
print(df["Communication_Level"].value_counts())


print("\nUpdated Dataset Shape:")
print(df.shape)


# --------------------------------------------------
# Generate Career Profile Features
# --------------------------------------------------

# Available target job roles
target_roles = [
    "Data Analyst",
    "Data Scientist",
    "Machine Learning Engineer",
    "AI Engineer",
    "Software Developer",
    "Data Engineer"
]


# Generate target role
target_role = np.random.choice(
    target_roles,
    size=NUM_STUDENTS,
    p=[
        0.20,
        0.20,
        0.20,
        0.15,
        0.15,
        0.10
    ]
)


# Map target roles to their corresponding domains
role_domain_mapping = {
    "Data Analyst": "Data Analytics",
    "Data Scientist": "Data Science",
    "Machine Learning Engineer": "AI/ML",
    "AI Engineer": "AI/ML",
    "Software Developer": "Software Development",
    "Data Engineer": "Data Engineering"
}


# Generate preferred domain based on target role
preferred_domain = np.array([
    role_domain_mapping[role]
    for role in target_role
])


# Add career profile features to DataFrame
df["Target_Role"] = target_role
df["Preferred_Domain"] = preferred_domain


# Display career profile information
print("\nCareer profile features generated successfully!")


print("\nFirst 5 Career Profile Records:")

print(
    df[
        [
            "Student_ID",
            "Target_Role",
            "Preferred_Domain"
        ]
    ].head()
)


print("\nTarget Role Distribution:")
print(df["Target_Role"].value_counts())


print("\nPreferred Domain Distribution:")
print(df["Preferred_Domain"].value_counts())


print("\nUpdated Dataset Shape:")
print(df.shape)


# --------------------------------------------------
# Create Placement Score
# --------------------------------------------------

# Convert categorical levels into numerical scores

dsa_score_mapping = {
    "Beginner": 0,
    "Intermediate": 1,
    "Advanced": 2
}

project_score_mapping = {
    "Basic": 0,
    "Intermediate": 1,
    "Advanced": 2
}

skill_score_mapping = {
    "None": 0,
    "Beginner": 1,
    "Intermediate": 2,
    "Advanced": 3
}

communication_score_mapping = {
    "Poor": 0,
    "Average": 1,
    "Good": 2,
    "Excellent": 3
}


# Convert features to numerical scores

dsa_numeric = df["DSA_Level"].map(dsa_score_mapping)

project_numeric = df["Major_Project_Level"].map(
    project_score_mapping
)

python_numeric = df["Python_Level"].map(
    skill_score_mapping
)

sql_numeric = df["SQL_Level"].map(
    skill_score_mapping
)

powerbi_numeric = df["PowerBI_Level"].map(
    skill_score_mapping
)

ml_numeric = df["MachineLearning_Level"].map(
    skill_score_mapping
)

statistics_numeric = df["Statistics_Level"].map(
    skill_score_mapping
)

deep_learning_numeric = df["DeepLearning_Level"].map(
    skill_score_mapping
)

communication_numeric = df["Communication_Level"].map(
    communication_score_mapping
)


# Create base placement score

placement_score = (

    # Academic performance
    (df["CGPA"] * 2.0)

    # Coding and DSA
    + (df["LeetCode_Problems"] * 0.015)
    + (dsa_numeric * 3.0)

    # Projects
    + (df["Total_Projects"] * 1.0)
    + (project_numeric * 2.0)
    + (df["Deployment_Experience"].map({"Yes": 2, "No": 0}))

    # Internship experience
    + (df["Internship_Count"] * 3.0)

    # Technical skills
    + (python_numeric * 1.5)
    + (sql_numeric * 1.2)
    + (powerbi_numeric * 0.8)
    + (ml_numeric * 1.5)
    + (statistics_numeric * 1.0)
    + (deep_learning_numeric * 1.0)

    # Professional profile
    + (df["Open_Source_Contribution"].map({"Yes": 1.5, "No": 0}))
    + (df["Portfolio_Website"].map({"Yes": 1.0, "No": 0}))

    # Certifications
    + (df["Industry_Certifications"] * 0.5)

    # Communication
    + (communication_numeric * 2.0)
)


# Add placement score temporarily to DataFrame

df["Placement_Score"] = np.round(
    placement_score,
    2
)


# Display placement score information

print("\nPlacement score generated successfully!")


print("\nFirst 5 Placement Score Records:")

print(
    df[
        [
            "Student_ID",
            "CGPA",
            "DSA_Level",
            "Total_Projects",
            "Internship_Count",
            "Communication_Level",
            "Placement_Score"
        ]
    ].head()
)


print("\nPlacement Score Statistics:")

print(df["Placement_Score"].describe())


print("\nUpdated Dataset Shape:")

print(df.shape)


# --------------------------------------------------
# Generate Placement Status Target Variable
# --------------------------------------------------

# Convert placement score into placement probability
placement_probability = 1 / (
    1 + np.exp(
        -(df["Placement_Score"] - 45) / 7
    )
)


# Generate placement outcome using probability
random_values = np.random.random(NUM_STUDENTS)

placement_status = np.where(
    random_values < placement_probability,
    "Placed",
    "Not Placed"
)


# Add target variable to DataFrame
df["Placement_Status"] = placement_status


# Display placement target information
print("\nPlacement status generated successfully!")


print("\nFirst 5 Placement Status Records:")

print(
    df[
        [
            "Student_ID",
            "Placement_Score",
            "Placement_Status"
        ]
    ].head()
)


print("\nPlacement Status Distribution:")

print(df["Placement_Status"].value_counts())


print("\nPlacement Status Percentage:")

print(
    df["Placement_Status"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)


print("\nUpdated Dataset Shape:")

print(df.shape)


# --------------------------------------------------
# Save Generated Dataset
# --------------------------------------------------

output_path = "data/student_placement_data.csv"

df.to_csv(
    output_path,
    index=False
)

print("\nDataset saved successfully!")

print(f"\nFile Location: {output_path}")

print("\nFinal Dataset Shape:")
print(df.shape)