# Import modules
from google import genai
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Retrieve the Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini Client
client = genai.Client(api_key=api_key)

# Send a prompt to Gemini
user_prompt = input("Ask Gemini : ")
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=user_prompt
)

# Print Gemini's response
print(response.text)