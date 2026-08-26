from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).resolve().parent.parent / ".env"

print("Looking for:", env_path)
print("Exists:", env_path.exists())

load_dotenv(env_path)

print("KEY =", os.getenv("GROQ_API_KEY"))