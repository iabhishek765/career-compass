CREATE TABLE IF NOT EXISTS assessment_reports (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    prediction TEXT NOT NULL,

    confidence REAL NOT NULL,

    career_report TEXT NOT NULL,

    career_path TEXT NOT NULL,

    recommended_courses TEXT NOT NULL,

    recommended_projects TEXT NOT NULL,

    recommended_certifications TEXT NOT NULL,

    skills_to_improve TEXT NOT NULL,

    student_answers TEXT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);