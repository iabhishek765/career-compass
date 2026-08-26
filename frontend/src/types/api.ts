export interface StudentRequest {
  Age: number;
  Gender: string;
  Branch: string;
  Graduation_Year: number;
  CGPA: number;
  LeetCode_Problems: number;
  DSA_Level: string;
  GitHub_Repositories: number;
  Open_Source_Contribution: string;
  Total_Projects: number;
  Major_Project_Level: string;
  AI_ML_Projects: number;
  Deployment_Experience: string;
  Internship_Count: number;
  Internship_Domain: string;
  Python_Level: string;
  SQL_Level: string;
  PowerBI_Level: string;
  MachineLearning_Level: string;
  Statistics_Level: string;
  DeepLearning_Level: string;
  LinkedIn_Profile: string;
  GitHub_Profile: string;
  Portfolio_Website: string;
  Industry_Certifications: number;
  Communication_Level: string;
  Target_Role: string;
  Preferred_Domain: string;
}

export interface RecommendationResponse {
  recommended_courses: string[];
  recommended_projects: string[];
  recommended_certifications: string[];
  missing_skills: string[];
  career_path: string[];
}

export interface PredictionResponse {
  report_id: number | null;
  prediction: string;
  probability: number;
  report: string;
  recommendations: RecommendationResponse;
}