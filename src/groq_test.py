import os
from dotenv import load_dotenv
from groq import Groq

# Load .env file
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

print("=" * 60)
print("CAREER COMPASS - GROQ CONNECTION TEST")
print("=" * 60)

# Check API Key
if not api_key:
    print("\nERROR: GROQ_API_KEY not found in .env")
    exit()

print("\nAPI Key Loaded Successfully")
print("Key starts with:", api_key[:10] + "********")

# Create Client
client = Groq(api_key=api_key)

print("\nConnecting to Groq...\n")

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": "Reply with exactly this sentence: Groq connection successful."
        }
    ],
    temperature=0
)

print("=" * 60)
print("MODEL RESPONSE")
print("=" * 60)

print(response.choices[0].message.content)