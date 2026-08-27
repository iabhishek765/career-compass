from pathlib import Path

from src.groq_client import GroqClient
from src.profile_analyzer import analyze_student


def generate_career_report(student_data, prediction, probability):
    """
    Generate a personalized AI career report using Groq.
    """

    try:
        # -------------------------------------------------
        # 1. Analyze student profile
        # -------------------------------------------------

        analysis = analyze_student(student_data)

        strengths = analysis.get("strengths", [])
        improvements = analysis.get("improvements", [])

        # Convert lists into readable text
        strengths_text = "\n".join(
            f"- {item}" for item in strengths
        )

        improvements_text = "\n".join(
            f"- {item}" for item in improvements
        )

        # -------------------------------------------------
        # 2. Load career report prompt
        # -------------------------------------------------

        prompt_path = (
            Path(__file__).resolve().parent.parent
            / "prompts"
            / "career_report_prompt.txt"
        )

        if not prompt_path.exists():
            raise FileNotFoundError(
                f"Prompt file not found: {prompt_path}"
            )

        system_prompt = prompt_path.read_text(
            encoding="utf-8"
        )

        # -------------------------------------------------
        # 3. Create user prompt
        # -------------------------------------------------

        user_prompt = f"""
Student Profile:

CGPA: {student_data.get("CGPA")}
DSA Level: {student_data.get("DSA_Level")}
Projects: {student_data.get("Projects")}
Internships: {student_data.get("Internships")}
SQL Level: {student_data.get("SQL_Level")}

Placement Prediction: {prediction}
Placement Probability: {probability}%

Profile Strengths:
{strengths_text}

Areas for Improvement:
{improvements_text}

Generate a concise, personalized career report for this student.

The report should:
- Mention the student's strongest areas.
- Mention the most important areas to improve.
- Give practical career advice.
- Be encouraging but realistic.
- Be suitable for displaying directly on a career dashboard.
- Do not mention that an AI generated the report.
"""

        # -------------------------------------------------
        # 4. Call Groq
        # -------------------------------------------------

        print("Generating AI career report...")

        groq_client = GroqClient()

        report = groq_client.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt
        )

        # -------------------------------------------------
        # 5. Validate response
        # -------------------------------------------------

        if not report:
            raise ValueError(
                "Groq returned an empty career report."
            )

        report = report.strip()

        print("AI career report generated successfully.")

        return report

    except Exception as e:
        print(f"ERROR generating career report: {e}")
        return f"Unable to generate career report: {e}"