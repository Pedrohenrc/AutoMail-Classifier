# 📧 AutoMail-Classifier

Sistema inteligente de classificação automática de emails utilizando Inteligência Artificial, desenvolvido com foco em arquitetura limpa, separação de responsabilidades e manutenibilidade.

## 📌 Visão Geral

O AutoMail-Classifier automatiza a triagem de emails corporativos, classificando mensagens e sugerindo respostas automáticas com base em IA.

O sistema aceita emails em diferentes formatos e aplica um fluxo bem definido de processamento, desde a entrada do usuário até a geração da resposta.

## 🧱 Arquitetura

O projeto segue os princípios da Clean Architecture, organizando o código em camadas bem definidas:

**Controller** (Interface / Web)

**Use Cases** (Regra de negócio)

**Ports** (Interfaces)

**Adapters** (Infraestrutura)

**Domain** (Entidades e Value Objects)

### Benefícios:

**Baixo** acoplamento

**Independência** de frameworks

Facilidade de **testes**

**Substituição simples** de serviços externos (IA, leitores de arquivo, etc.)

## 🔄 Fluxo da Aplicação

1. Fluxo simplificado baseado na arquitetura implementada:

    * Usuário

    * Envia texto ou arquivo pelo formulário web

2. Controller (FastAPI)

    * Recebe a requisição

    * Valida entrada

    * Orquestra o fluxo

3. FileReaderFactory

    * Decide qual leitor usar (PdfReader ou TxtReader)
    
    * Extrai o conteúdo textual do arquivo

4. AnalyzeEmailUseCase

    * Coordena o processo de classificação
    
    * Não depende de detalhes de infraestrutura

5. GeminiClassifier
    
    * Classifica o email (Produtivo / Improdutivo)

6. GeminiResponse
    
    * Gera a resposta sugerida

7. Controller
    
    * Retorna o resultado para o frontend

8. Frontend

    * Exibe a classificação e a resposta ao usuário
    
    * Esse fluxo garante que frameworks e serviços externos nunca contaminem a regra de negócio.

## 🛠️ Tecnologias Utilizadas
### Backend

* Python 3.11+

* FastAPI

* Uvicorn

### Frontend

* HTML5

* CSS

* JavaScript

* Jinja2

## Inteligência Artificial

* Google Gemini API

  * Modelo: gemini-2.5-flash

## Processamento de Arquivos

* Pypdf

* Leitura de arquivos .txt

## ⚙️ Configuração do Ambiente
### 🔑 API Key do Gemini

Para que o sistema funcione corretamente, é necessário configurar uma **API Key do Google Gemini.**

**Passo a passo:**

1. Acesse:
    - https://aistudio.google.com/app/apikey

3. Gere uma nova API Key

4. Configure a variável de ambiente conforme o ambiente de execução

## ▶️ Instalação e Execução Local
### 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/AutoMail-Classifier.git
cd AutoMail-Classifier
```

2️⃣ Crie o ambiente virtual

```bash
python -m venv venv
```

Ative:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Crie um arquivo .env na raiz do projeto:

```env
GEMINI_API_KEY=sua_api_key_aqui
```

### 5️⃣ Execute a aplicação

```bash
uvicorn app.main:app --reload
```

A aplicação estará disponível em:

```arduino
http://localhost:8000
```

### 🧪 Como Utilizar

1. Acesse a página inicial

2. Insira o email:
   - Texto direto  
   **ou**
   - Upload de arquivo .txt ou .pdf

3. Envie para análise

4. Visualize:
    - Classificação do email
    - Resposta sugerida

## ⭐ Diferenciais Técnicos
* Clean Architecture aplicada na prática
* Use Cases independentes de frameworks
* Adapters desacoplados
* Fácil extensão para novos formatos de arquivo
* Fácil troca de provedor de IA
* Código orientado a regras de negócio

## 📄 Licença

Projeto desenvolvido **como case técnico** para processo seletivo.

## 👨‍💻 Autor

Pedro Henrique Carvalho Sousa

GitHub: [@pedrohenrc](https://github.com/pedrohenrc)

LinkedIn: [in/pedro-sousa-dev](https://linkedin.com/in/pedro-sousa-dev)

## 🙏 Agradecimentos

Comunidade FastAPI

Google Gemini

Princípios de Clean Architecture
