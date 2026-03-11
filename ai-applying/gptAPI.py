import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def chat(user_message: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a experienced software engineer. Return only clean and qualified code. Don't return any other text."},
            {"role": "user", "content": user_message},
        ],
    )

    return response.choices[0].message.content

print(chat("Write a hello world program in Python"))