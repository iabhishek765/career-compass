export interface HistoryReport {
  id: number;
  created_at: string;
  prediction: string;
  confidence: number;
}

export interface HistoryReportDetail extends HistoryReport {
  career_report: string;
  career_path: string[];
  recommended_courses: string[];
  recommended_projects: string[];
  recommended_certifications: string[];
  skills_to_improve: string[];
  student_answers: Record<string, string | number | undefined>;
}