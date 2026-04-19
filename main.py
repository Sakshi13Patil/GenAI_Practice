import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

print(f"OpenAI API Key: {'Yes' if OPENAI_API_KEY else 'No'}")
print(f"GEMINI API Key: {'Yes' if GEMINI_API_KEY else 'No'}")
print(f"CLAUDE API Key: {'Yes' if CLAUDE_API_KEY else 'No'}")
print(f"DEEPSEEK API Key: {'Yes' if DEEPSEEK_API_KEY else 'No'}")