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

```


---

# 🏗️ Project Architecture

Career Compass follows a modular architecture that separates the frontend, backend, machine learning components, data, experimentation, and supporting resources.

```text
Career_Compass/
│
├── app/                         # FastAPI backend
│   ├── routes/                  # API endpoints
│   ├── schemas/                # Request / response schemas
│   └── services/               # Backend application services
│
├── frontend/                    # Next.js frontend
│   ├── src/
│   │   ├── features/            # Feature-specific UI modules
│   │   ├── services/            # Frontend API / service logic
│   │   ├── types/               # TypeScript types
│   │   └── lib/                 # Shared frontend utilities
│   ├── public/                  # Static frontend assets
│   └── package.json             # Frontend dependencies
│
├── data/                        # Dataset and data resources
│
├── models/                      # Trained ML models
│
├── notebooks/                   # Experiments and analysis
│
├── prompts/                     # AI prompt templates
│
├── reports/                     # Project reports and documentation
│
├── repositories/                # Data / repository utilities
│
├── sql/                         # SQL resources and queries
│
├── src/                         # Core ML / data processing code
│
├── .gitignore                   # Git ignore rules
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
└── career_compass.db            # Local application database
```

### Architecture Principles

- **Separation of concerns** — frontend, backend, ML, and data components are independently organized.
- **Modular services** — prediction, validation, and recommendation logic are separated into dedicated services.
- **API-driven communication** — the frontend communicates with the backend through REST APIs.
- **Reusable ML inference** — the trained model is loaded for inference instead of retraining per request.
- **Experimentation isolation** — notebooks and experiments are separated from application code.

---


## 🛠️ Technology Stack

### Frontend
- Next.js
- React
- TypeScript
- Tailwind CSS


### Backend
- Python
- FastAPI
- Pydantic
- Uvicorn


### Machine Learning
- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib


### AI Layer
- LLM-based career report generation
- Prompt engineering
- Structured model output


### Data & Storage
- SQLite
- CSV / structured datasets


### Development Tools
- Git
- GitHub
- VS Code
- Jupyter Notebook


---

# 🔬 Machine Learning Pipeline

The machine learning component follows a structured training and inference pipeline.

### Training Pipeline

```text
┌─────────────────────┐
│   Raw Student Data  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    Data Cleaning    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Feature Engineering │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Feature Validation │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Model Training    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Model Evaluation  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│     Best Model      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Prediction Service  │
└─────────────────────┘
```

### Inference

The trained model is loaded by the backend and used through the prediction service. A new model is **not trained every time** a student submits an assessment.

The inference flow is:

```text
Student Profile
      │
      ▼
Feature Validation
      │
      ▼
Feature Processing
      │
      ▼
Trained ML Model
      │
      ▼
Prediction
      │
      ▼
Recommendation Engine
      │
      ▼
Career Report
```

This separation keeps model training and production inference as independent stages.


---

# 📊 Prediction & Recommendation Flow

A student's profile is first validated and processed before being passed to the prediction service.

```text
┌──────────────────────┐
│   Student Request    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Pydantic Validation  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Feature Processing   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│      ML Model        │
└──────────┬───────────┘
           │
           ├──────────────► Prediction
           │
           └──────────────► Confidence / Probability
                              │
                              ▼
                    ┌──────────────────────┐
                    │ Recommendation       │
                    │       Engine         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ AI-Assisted Career   │
                    │       Report         │
                    └──────────────────────┘
```

The architecture keeps the prediction logic separate from the presentation and recommendation layers. This makes the system easier to maintain, test, and extend.
     

---

# 🎨 User Experience

The frontend is designed around a simple flow:

01 — **Understand**

Learn what Career Compass evaluates and how the platform works.

02 — **Assess**

Provide academic, technical, experience, and profile information.

03 — **Analyze**

The system processes the submitted profile through the ML pipeline.

04 — **Improve**

Receive skill-gap insights and personalized recommendations.

05 — **Plan**

Use the generated career report to decide what to work on next.


---

# ⚙️ Local Setup

1. **Clone the repository**

git clone https://github.com/iabhishek765/career-compass.git
cd career-compass

##  🐍 Backend Setup

2. **Create a Python virtual environment:**

python -m venv venv

Windows
venv\Scripts\activate

macOS / Linux
source venv/bin/activate

3. **Install dependencies:**

pip install -r requirements.txt

4. **Start the FastAPI server:**

python -m uvicorn app.main:app --reload

The backend will be available at:

http://127.0.0.1:8000

FastAPI documentation:

http://127.0.0.1:8000/docs

## 💻 Frontend Setup

5. **Move into the frontend directory:**

cd frontend

Install dependencies:

npm install

6. **Start the development server:**

npm run dev

The frontend will normally be available at:

http://localhost:3000

# 🔗 API

The frontend communicates with the FastAPI backend through a prediction endpoint.

### Prediction Endpoint

```text
POST /predict
```

The endpoint accepts a validated student profile and returns:

- Placement / career-readiness prediction
- Prediction probability / confidence
- Skill-gap analysis
- Personalized recommendations
- AI-assisted career report

### Request Flow

```text
┌──────────────────┐
│     Frontend     │
│    Next.js UI    │
└────────┬─────────┘
         │
         │ POST /predict
         ▼
┌──────────────────┐
│  FastAPI Backend │
│   API Endpoint   │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Feature / Input  │
│    Validation    │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Prediction       │
│    Service       │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│   ML Prediction  │
│      Model       │
└────────┬─────────┘
         │
         ├──────────────► Prediction
         │
         ▼
┌──────────────────┐
│ Skill Gap &      │
│ Recommendation   │
│     Engine       │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ AI-Assisted      │
│ Career Report    │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Frontend Career  │
│      Report      │
└──────────────────┘
```

### Local Development

Backend:

```bash
python -m uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

Frontend:

```bash
cd frontend
npm install
npm run dev
```

Frontend URL:

```text
http://localhost:3000
```

# 🧪 Development & Experiments

The notebooks/ directory contains experimentation and analysis work used during development.

These notebooks help document:

- Data exploration
- Feature analysis
- Model experiments
- Evaluation
- ML development decisions

This separation keeps experimentation separate from the production prediction pipeline.

--- 

# 🛡️ Important ML Design Consideration

A major consideration during development was avoiding target leakage.

Features that directly represent or derive from the prediction target should not be used as model inputs.

For example, a synthetic placement score used during dataset generation should not simply be passed into the model to predict placement status.

The goal is to ensure that model performance represents meaningful relationships within the student profile rather than information that directly reveals the target.


---

# 🎯 Project Goals

Career Compass was designed with three main goals:

1. **Prediction**
Estimate a student's current career / placement readiness.

2. **Explanation**
Help students understand the strengths and gaps behind the prediction.

3. **Action**
Convert the analysis into practical next steps.


---


# 🚧 Current Status

### Completed
- Student profile assessment
- ML prediction pipeline
- Feature validation
- Skill-gap analysis
- Recommendation engine
- AI-assisted career reporting
- FastAPI backend
- Next.js frontend
- Career Compass landing page
- GitHub repository
- Production deployment
- Automated testing
- Authentication
- Persistent user accounts
- Production database

 ### In Progress
- Production deployment
- Automated testing
- Authentication
- Persistent user accounts
- Production database


 ---

 # 🔮 Future Improvements

 Possible future improvements include:

- User authentication and profiles
- Historical assessment tracking
- Improved model explainability
- Model monitoring
- More diverse training data
- Automated model retraining
- Career-specific prediction models
- Interactive skill-roadmap generation
- Resume analysis
- Job-role matching
- Job-market integration
- Personalized learning-resource recommendations

---

# 🌐 Project Links

GitHub:
https://github.com/iabhishek765/career-compass

Live Demo:
Coming soon.

---


# 📚 What I Learned

Building Career Compass involved working across multiple areas of software and machine learning engineering:

- Designing an end-to-end ML application
- Feature engineering and validation
- Avoiding target leakage
- Building REST APIs with FastAPI
- Connecting a frontend with an ML backend
- Structuring ML inference services
- Designing recommendation systems
- Integrating LLM-assisted reporting
- Working with Next.js and TypeScript
- Managing a project with Git and GitHub
- Separating experimentation from production code


---

# 👨‍💻 Author

Abhishek

B.Tech Computer Science Engineering — AI & ML

Interested in:

- Artificial Intelligence
- Machine Learning
- Data Science
- ML Engineering
- AI-powered applications


---

# ⭐ If you find this project interesting

Feel free to explore the repository, review the implementation, and share feedback.

