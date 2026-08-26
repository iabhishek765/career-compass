import { Question } from "../types";

export const questions: Question[] = [
  // =====================================================
  // SECTION 1 — ACADEMIC PROFILE
  // =====================================================

  {
    id: 1,
    field: "Age",
    question: "What is your age?",
    type: "number",
    section: 1,
    required: true,
    min: 16,
    max: 35,
    step: 1,
    placeholder: "Enter your age (16–35)",
  },

  {
    id: 2,
    field: "Gender",
    question: "What is your gender?",
    type: "select",
    section: 1,
    required: true,
    options: ["Male", "Female", "Other"],
  },

  {
    id: 3,
    field: "Branch",
    question: "What is your engineering branch?",
    type: "select",
    section: 1,
    required: true,
    options: ["CSE", "IT", "ECE", "EEE", "Mechanical", "Civil", "Other"],
  },

  {
    id: 4,
    field: "Graduation_Year",
    question: "What is your graduation year?",
    type: "select",
    section: 1,
    required: true,
    options: ["2024", "2025", "2026", "2027", "2028", "2029"],
  },

  {
    id: 5,
    field: "CGPA",
    question: "What is your current CGPA?",
    type: "number",
    section: 1,
    required: true,
    min: 0,
    max: 10,
    step: 0.01,
    placeholder: "Enter your CGPA (0–10)",
  },

  // =====================================================
  // SECTION 2 — CODING & TECHNICAL SKILLS
  // =====================================================

  {
    id: 6,
    field: "LeetCode_Problems",
    question: "How many LeetCode problems have you solved?",
    type: "number",
    section: 2,
    required: true,
    min: 0,
    max: 4000,
    step: 1,
    placeholder: "Enter problems solved (0–4000)",
  },

  {
    id: 7,
    field: "DSA_Level",
    question: "What is your DSA proficiency level?",
    type: "select",
    section: 2,
    required: true,
    options: ["Beginner", "Intermediate", "Advanced"],
  },

  {
    id: 8,
    field: "Python_Level",
    question: "What is your Python proficiency level?",
    type: "select",
    section: 2,
    required: true,
    options: ["Beginner", "Intermediate", "Advanced"],
  },

  {
    id: 9,
    field: "SQL_Level",
    question: "What is your SQL proficiency level?",
    type: "select",
    section: 2,
    required: true,
    options: ["Beginner", "Intermediate", "Advanced"],
  },

  {
    id: 10,
    field: "PowerBI_Level",
    question: "What is your Power BI proficiency level?",
    type: "select",
    section: 2,
    required: true,
    options: ["Beginner", "Intermediate", "Advanced"],
  },

  // =====================================================
  // SECTION 3 — AI/ML & PROJECTS
  // =====================================================

  {
    id: 11,
    field: "MachineLearning_Level",
    question: "What is your Machine Learning proficiency level?",
    type: "select",
    section: 3,
    required: true,
    options: ["Beginner", "Intermediate", "Advanced"],
  },

  {
    id: 12,
    field: "Statistics_Level",
    question: "What is your Statistics proficiency level?",
    type: "select",
    section: 3,
    required: true,
    options: ["Beginner", "Intermediate", "Advanced"],
  },

  {
    id: 13,
    field: "DeepLearning_Level",
    question: "What is your Deep Learning proficiency level?",
    type: "select",
    section: 3,
    required: true,
    options: ["Beginner", "Intermediate", "Advanced"],
  },

  {
    id: 14,
    field: "Total_Projects",
    question: "How many technical projects have you completed?",
    type: "number",
    section: 3,
    required: true,
    min: 0,
    max: 50,
    step: 1,
    placeholder: "Enter total projects (0–50)",
  },

  {
    id: 15,
    field: "Major_Project_Level",
    question: "What is the complexity level of your strongest project?",
    type: "select",
    section: 3,
    required: true,
    options: ["Beginner", "Intermediate", "Advanced"],
  },

  {
    id: 16,
    field: "AI_ML_Projects",
    question: "How many AI/ML projects have you completed?",
    type: "number",
    section: 3,
    required: true,
    min: 0,
    max: 50,
    step: 1,
    placeholder: "Enter AI/ML projects (0–50)",
  },

  // =====================================================
  // SECTION 4 — EXPERIENCE & PROFESSIONAL PROFILE
  // =====================================================

  {
    id: 17,
    field: "GitHub_Repositories",
    question: "How many GitHub repositories do you have?",
    type: "number",
    section: 4,
    required: true,
    min: 0,
    max: 500,
    step: 1,
    placeholder: "Enter number of repositories (0–500)",
  },

  {
    id: 18,
    field: "Open_Source_Contribution",
    question: "Have you contributed to open-source projects?",
    type: "select",
    section: 4,
    required: true,
    options: ["Yes", "No"],
  },

  {
    id: 19,
    field: "Deployment_Experience",
    question: "Do you have experience deploying applications or ML models?",
    type: "select",
    section: 4,
    required: true,
    options: ["Yes", "No"],
  },

  {
    id: 20,
    field: "Internship_Count",
    question: "How many internships have you completed?",
    type: "number",
    section: 4,
    required: true,
    min: 0,
    max: 10,
    step: 1,
    placeholder: "Enter internship count (0–10)",
  },

  {
    id: 21,
    field: "Internship_Domain",
    question: "What was your primary internship domain?",
    type: "select",
    section: 4,
    required: true,
    options: [
      "None",
      "AI/ML",
      "Data Science",
      "Data Analytics",
      "Software Development",
      "Web Development",
      "Cloud/DevOps",
      "Cybersecurity",
      "Other",
    ],
  },

  {
    id: 22,
    field: "LinkedIn_Profile",
    question: "Do you have an updated LinkedIn profile?",
    type: "select",
    section: 4,
    required: true,
    options: ["Yes", "No"],
  },

  {
    id: 23,
    field: "GitHub_Profile",
    question: "Do you have an active GitHub profile?",
    type: "select",
    section: 4,
    required: true,
    options: ["Yes", "No"],
  },

  {
    id: 24,
    field: "Portfolio_Website",
    question: "Do you have a portfolio website?",
    type: "select",
    section: 4,
    required: true,
    options: ["Yes", "No"],
  },

  {
    id: 25,
    field: "Industry_Certifications",
    question: "How many industry certifications have you completed?",
    type: "number",
    section: 4,
    required: true,
    min: 0,
    max: 30,
    step: 1,
    placeholder: "Enter number of certifications (0–30)",
  },

  // =====================================================
  // SECTION 5 — CAREER PREFERENCES
  // =====================================================

  {
    id: 26,
    field: "Communication_Level",
    question: "How would you rate your communication skills?",
    type: "select",
    section: 5,
    required: true,
    options: ["Beginner", "Intermediate", "Advanced"],
  },

  {
    id: 27,
    field: "Target_Role",
    question: "What is your target career role?",
    type: "select",
    section: 5,
    required: true,
    options: [
      "AI/ML Engineer",
      "Data Scientist",
      "Data Analyst",
      "Software Engineer",
      "Data Engineer",
      "Business Analyst",
      "Other",
    ],
  },

  {
    id: 28,
    field: "Preferred_Domain",
    question: "What is your preferred career domain?",
    type: "select",
    section: 5,
    required: true,
    options: [
      "Artificial Intelligence",
      "Machine Learning",
      "Data Science",
      "Data Analytics",
      "Software Development",
      "Cloud/DevOps",
      "Cybersecurity",
      "Other",
    ],
  },
];