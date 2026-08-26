from groq_client import GroqClient
from prompt_loader import load_prompt


print("=" * 60)
print("GROQ CLIENT TEST")
print("=" * 60)

system_prompt = load_prompt("career_report_prompt.txt")

user_prompt = """
Prediction:
Placed

Confidence:
94%

Strengths:
High CGPA
Strong DSA
Good Projects

Improvement Areas:
Statistics
SQL

Student Goal:
ML Engineer
"""

client = GroqClient()

response = client.generate(
    system_prompt,
    user_prompt
)

print(response)