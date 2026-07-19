import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise Exception("OPENROUTER_API_KEY not found in .env")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

def ask_gemini(question):
    response = client.chat.completions.create(
      model="openai/gpt-oss-20b:free",
        messages=[
            {
                "role": "system",
                "content": "You are SmartFinance AI, a helpful personal finance assistant."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.choices[0].message.content