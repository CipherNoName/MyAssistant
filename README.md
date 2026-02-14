# MyAssistant

Assistente virtual em desenvolvimento, focado em aprendizado, automação, experimentação e integração com inteligência artificial.  
Este projeto permite que você interaja por voz, usando reconhecimento de fala e síntese de voz, enquanto se conecta a APIs de IA externas para processar informações e gerar respostas.

---
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
git clone https://github.com/seu-usuario/MyAssistant.git
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

