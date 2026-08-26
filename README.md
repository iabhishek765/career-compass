# 🎯 Career Compass

### AI-Powered Career Guidance & Placement Intelligence Platform

Career Compass is an AI-powered career guidance platform that analyzes a student's academic background, technical skills, experience, interests, and assessment profile to generate a data-driven view of their career readiness.

The system combines **Machine Learning, skill-gap analysis, rule-based recommendations, and AI-assisted career reporting** to help students understand where they currently stand and what they should focus on next.

---

## 🚀 Overview

Choosing a career path can be difficult when students do not have a clear understanding of their strengths, weaknesses, and current skill level.

Career Compass aims to solve this problem by transforming a student's profile into an actionable career report.

The platform evaluates the student's profile and provides:

- 📊 ML-based placement prediction
- 🔎 Profile and skill analysis
- 🧩 Skill-gap identification
- 🎯 Personalized career recommendations
- 📚 Learning direction and next-step suggestions
- 🤖 AI-assisted career report generation

Instead of simply showing a prediction, Career Compass focuses on explaining **what the prediction means and what the student can do next.**

---

## ✨ Key Features

### 1. ML-Based Career Prediction

The system analyzes student profile features using a trained machine learning model to estimate placement readiness.

The prediction pipeline is designed to separate:

**Input Profile → Feature Validation → ML Prediction → Recommendation Layer → Career Report**

---

### 2. Skill Gap Analysis

Career Compass identifies areas where a student can improve their profile.

Examples include:

- Technical skills
- DSA / problem-solving ability
- Projects
- Certifications
- Internship experience
- Academic performance
- Other career-readiness indicators

The goal is not only to identify weaknesses but to convert them into actionable improvement areas.

---

### 3. Personalized Recommendations

Recommendations are generated based on the student's individual profile rather than providing the same roadmap to every student.

The system can suggest:

- Skills to strengthen
- Areas to practice
- Projects to build
- Learning directions
- Career preparation priorities

---

### 4. AI-Assisted Career Report

The platform can transform the structured ML analysis into a concise, personalized career report.

The AI layer is used for **interpreting and communicating the analysis**, while the core prediction remains driven by the machine learning pipeline.

This separation helps keep the system more structured and explainable.

---

### 5. Student Profile Analysis

Career Compass considers multiple dimensions of a student's profile, including:

- Academic performance
- Technical skills
- Coding / DSA experience
- Projects
- Internships
- Certifications
- Experience
- Career-related assessment inputs

---

# 🧠 How Career Compass Works

```text
                    Student Profile
                          │
                          ▼
                ┌───────────────────┐
                │   Input /         │
                │   Assessment      │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Feature           │
                │ Validation        │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Machine Learning  │
                │ Prediction Model   │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Skill Gap &       │
                │ Recommendation    │
                │ Engine            │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ AI-Assisted       │
                │ Career Report     │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Personalized      │
                │ Career Guidance   │
                └───────────────────┘


# 🏗️ Project Architecture

Career_Compass/
│
├── app/                    # FastAPI application
│   ├── routes/             # API endpoints
│   ├── schemas/            # Request/response schemas
│   └── services/           # Application services
│
├── frontend/               # Next.js frontend
│   ├── src/
│   │   ├── features/
│   │   ├── services/
│   │   ├── types/
│   │   └── lib/
│   ├── public/
│   └── package.json
│
├── data/                   # Dataset and data resources
│
├── models/                 # Trained ML models
│
├── notebooks/              # Experiments and analysis
│
├── prompts/                # AI prompt templates
│
├── reports/                # Project reports and documentation
│
├── repositories/           # Data / repository utilities
│
├── sql/                    # SQL resources and queries
│
├── src/                    # Core ML / data processing code
│
├── .gitignore
├── README.md
└── career_compass.db