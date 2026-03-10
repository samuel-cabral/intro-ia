import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def chat(user_message: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um assistente útil."},
            {"role": "user", "content": user_message},
        ],
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    user_input = input("Você: ")
    reply = chat(user_input)
    print(f"GPT: {reply}")
