# MyAssistant

Assistente virtual em desenvolvimento, focado em aprendizado, automação, experimentação e integração com inteligência artificial.  
Este projeto permite que você interaja por voz, usando reconhecimento de fala e síntese de voz, enquanto se conecta a APIs de IA externas para processar informações e gerar respostas.

---

## Como funciona

- O assistente envia perguntas do usuário para a API externa e recebe respostas em tempo real.  
- A comunicação com a API é feita via **HTTP** usando a biblioteca `requests`.  
- Para que o assistente funcione, é necessário ter uma **chave de API** válida, que deve ser adicionada no arquivo `.env` como:



API_KEY="Sua chave aqui"

---

Este arquivo serve como referência para **entender como o projeto funciona e como lidar com possíveis mudanças na API**.  
## Configuração da API

Para que o assistente funcione corretamente, você precisa fornecer uma **chave de API**.  

1. Crie um arquivo chamado `.env`:

```bash
touch .env       # Linux/macOS
# ou no Windows PowerShell:
# type nul > .env
``` 

## Instalação

Siga os passos abaixo para configurar o ambiente e instalar todas as dependências necessárias:

1. **Clone o repositório** (caso ainda não tenha feito):

```bash
git clone https://github.com/CipherNoName/MyAssistant.git
cd MyAssistant
```

2. **Crie e ative um ambiente virtual** (recomendado para isolar dependências do projeto):

```bash
python -m venv venv          # cria a venv
source venv/bin/activate     # Linux/macOS ou no Windows PowerShell: venv\Scripts\Activate.ps1
```

3. **Instale as dependências necessárias para rodar o assistente:**

```bash
pip install -r requirements.txt 
```

## Execução

**Com o ambiente ativado, você pode rodar o assistente diretamente:**

```bash
python main.py # rode dentro da venv
```

