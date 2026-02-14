# Sobre o MyAssistant

Este projeto é um **assistente virtual em Python**, que permite interagir por voz utilizando uma **API de Inteligência Artificial** para gerar respostas.  

---

## Como funciona

- O assistente envia perguntas do usuário para a API externa e recebe respostas em tempo real.  
- A comunicação com a API é feita via **HTTP** usando a biblioteca `requests`.  
- Para que o assistente funcione, é necessário ter uma **chave de API** válida, que deve ser adicionada no arquivo `.env` como:



API_KEY="Sua chave aqui"


- O projeto atualmente usa o modelo:  


https://openrouter.ai/api/v1/chat/completions

com o modelo `"arcee-ai/trinity-large-preview:free"`.

---

## Limitações

1. A **IA usada pode não estar mais disponível gratuitamente**.  
2. Caso o modelo atual deixe de funcionar ou não esteja mais disponível:
   - Verifique se você tem uma **conta válida no serviço da API** (ex: OpenRouter).  
   - Sua **chave de API (API_KEY)** geralmente funciona para todos os modelos disponíveis dentro da sua conta. **Você não precisa criar uma nova chave a menos que a antiga esteja perdida ou expirada.**  
   - Se o modelo configurado no código não estiver mais ativo, **substitua apenas o nome do modelo no JSON** pelo modelo equivalente disponível na API.  
     ```python
     # Exemplo:
     json={
         "model": "arcee-ai/trinity-large-preview:free",  # modelo antigo
         "messages": mensagens + [{"role": "user", "content": texto_usuario}],
         "max_tokens": 80
     }

     # Se o modelo não existir mais, troque para outro disponível:
     json={
         "model": "arcee-ai/trinity-large-v2",  # modelo substituto
         "messages": mensagens + [{"role": "user", "content": texto_usuario}],
         "max_tokens": 80
     }
     ```
---

## Observações

- O projeto depende de conexão com a internet para se comunicar com a API.  
- Para modificar ou testar outros modelos da API, revise a documentação do serviço para ajustar os parâmetros JSON corretamente.  
- O código está preparado para ser integrado com voz (usando `pyttsx3` e `SpeechRecognition`), mas você também pode adaptá-lo apenas para texto.  

---

Este arquivo serve como referência para **entender como o projeto funciona e como lidar com possíveis mudanças na API**.  
