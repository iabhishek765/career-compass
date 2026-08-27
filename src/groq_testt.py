from src.groq_client import GroqClient


client = GroqClient()

response = client.generate(
    "You are a helpful AI assistant.",
    "Explain machine learning in two sentences."
)

print("\n--- GROQ RESPONSE ---")
print(response)