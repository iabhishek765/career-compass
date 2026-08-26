import os

from dotenv import load_dotenv
from groq import Groq

from pathlib import Path

env_path = Path(__file__).resolve().parent / ".env"

print("Loading:", env_path)

load_dotenv(env_path)


class GroqClient:

    def __init__(self):

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY not found in .env")

        self.client = Groq(api_key=api_key)

    def generate(self, system_prompt, user_prompt):

        response = self.client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],

            temperature=0.3,

            max_tokens=350
        )

        return response.choices[0].message.content