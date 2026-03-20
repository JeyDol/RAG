import os

from dotenv import load_dotenv
from gigachat import GigaChat

load_dotenv()

def ask_llm(question: str, context: list[str]) -> str:
    context_text = "\n\n".join(context)

    prompt = f"""Ты helpful ассистент. Отвечай только на основе предоставленного контекста.

    Контекст:
    {context_text}

    Вопрос: {question}

    Ответ:"""

    with GigaChat(credentials=os.getenv("AUTHORIZATION_KEY"), verify_ssl_certs=False) as giga:
        response = giga.chat(prompt)
        return response.choices[0].message.content