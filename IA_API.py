import requests
from gtts import gTTS


API_KEY = "API_Key"

while True:
    texto_usuario = input("Digite sua pergunta aqui: ")

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": "arcee-ai/trinity-large-preview:free",
            "messages": [
                {
                    "role": "user",
                    "content": texto_usuario
                }
            ],
            "max_tokens": 80
        }
    )


    # Garantir que a resposta é JSON
    if response.headers.get("content-type", "").startswith("application/json"):
        dados = response.json()
        resposta = dados["choices"][0]["message"]["content"]
        print("Jarvis:", resposta)


