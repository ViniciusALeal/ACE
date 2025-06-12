from google import genai
from dotenv import load_dotenv
import os


load_dotenv()


API_KEY = os.getenv("GOOGLE_API_KEY")

def resposta_llm(pergunta):
    if not API_KEY:
        raise ValueError("Chave da API não encontrada. Verifique o arquivo .env.")

    client = genai.Client(api_key=API_KEY)

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=pergunta
    )
    return response.text

