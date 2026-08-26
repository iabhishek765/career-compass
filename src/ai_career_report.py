from src.prompt_loader import load_prompt
from src.groq_client import GroqClient
from src.profile_analyzer import analyze_student


def generate_career_report(student_data, prediction, probability):
    """
    Generate a professional AI career report using Groq.
    """

    # -----------------------------------------
    # Analyze Student Profile
    # -----------------------------------------

    analysis = analyze_student(student_data)

    strengths = analysis["strengths"]
    improvements = analysis["improvements"]

    # -----------------------------------------
    # Convert lists into readable text
    # -----------------------------------------

    strengths_text = "\n".join(
        f"- {item}" for item in strengths
    )

    improvements_text = "\n".join(
        f"- {item}" for item in improvements
    )

    # -----------------------------------------
    # Load System Prompt
    # -----------------------------------------

    system_prompt = load_prompt(
        "career_report_prompt.txt"
    )

    # -----------------------------------------
    # Build User Prompt
    # -----------------------------------------

    user_prompt = f"""
Placement Prediction:
{prediction}

Prediction Confidence:
{probability:.2f}%

Student Strengths:
{strengths_text}

Student Improvement Areas:
{improvements_text}

Complete Student Profile:

{student_data}

Generate a personalized career report.
"""

    # -----------------------------------------
    # Generate Report
    # -----------------------------------------

    client = GroqClient()

    report = client.generate(
        system_prompt,
        user_prompt
    )

    return report