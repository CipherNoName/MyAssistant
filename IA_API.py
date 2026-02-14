import requests
import os
from dotenv import load_dotenv
load_dotenv()  # lê o .env
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY não encontrada! Verifique seu arquivo .env")


def entrada(): # Optei por deixar no codigo mais atualmente estou usando outro metodo para comunicar com api
    return input("Digite sua pergunta aqui: ")

def perguntar_api(texto_usuario):
    mensagens = [
        {
            "role": "system", 
            "content": "Você sempre deve responder sem emojis ou símbolos." 
        },

     ]

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
            },

        json={
            "model": "arcee-ai/trinity-large-preview:free",
            "messages": mensagens + [

                {
                    "role": "user",
                    "content": texto_usuario
                }
            ],
            "max_tokens": 80
        }
    )

    return response


def saida(response):    # Garantir que a resposta é JSON
        dados = response.json()
        resposta = dados["choices"][0]["message"]["content"]
        return resposta


