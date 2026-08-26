from pydantic import BaseModel


class StudentRequest(BaseModel):
    Age: int
    Gender: str
    Branch: str
    Graduation_Year: int
    CGPA: float
    LeetCode_Problems: int
    DSA_Level: str
    GitHub_Repositories: int
    Open_Source_Contribution: str
    Total_Projects: int
    Major_Project_Level: str
    AI_ML_Projects: int
    Deployment_Experience: str
    Internship_Count: int
    Internship_Domain: str
    Python_Level: str
    SQL_Level: str
    PowerBI_Level: str
    MachineLearning_Level: str
    Statistics_Level: str
    DeepLearning_Level: str
    LinkedIn_Profile: str
    GitHub_Profile: str
    Portfolio_Website: str
    Industry_Certifications: int
    Communication_Level: str
    Target_Role: str
    Preferred_Domain: str