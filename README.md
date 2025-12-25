# AI-Bot 🩺

An intelligent AI-powered medical chatbot designed to answer health-related queries using uploaded bio-medical encyclopedias and domain-specific knowledge. Built using **Llama-3 (via Groq)**, **Hugging Face Inference API**, **LangChain**, **Pinecone vector database**, and **Flask**, this bot provides accurate, ultra-fast, and context-aware responses to user queries.

### 🔴 **Live Demo:** [✨️](https://doc-ai-51j0.onrender.com)

---

## 🚀 Features
* **Natural Language Medical Query Understanding:** Capable of interpreting complex medical questions.
* **Ultra-Fast Inference:** Powered by **Llama-3 via Groq** for near-instant responses.
* **RAG Architecture:** Uses Retrieval-Augmented Generation to ground answers in verified medical texts.
* **Cost-Efficient Embeddings:** Utilizes **Hugging Face Inference API** for lightweight, cloud-based embeddings (No heavy local download).
* **Vector Search:** efficient document retrieval using **Pinecone**.
* **Seamless Cloud Deployment:** deployed live on **Render**.

## 🛠 Tech Stack
* **Language:** Python 3.10
* **Framework:** Flask
* **Orchestration:** LangChain
* **LLM:** Llama-3 (via Groq API)
* **Embeddings:** Sentence-Transformers (via Hugging Face Inference Client)
* **Vector Database:** Pinecone
* **Deployment:** Render

## 📘 Use Case
Upload bio-medical books (PDFs) and interact with the bot to get accurate medical insights, references, and intelligent answers grounded in trusted data sources rather than generic AI hallucinations.

---

## 💻 How to run locally?

### STEPS:

**1. Clone the repository**
```bash
git clone https://github.com/BleeGleeWee/AI-Bot.git
cd AI-Bot
```

2. Create a conda environment
```bash
conda create -n AiBot python=3.10 -y
conda activate AiBot
```

4. Install the requirements
```bash
pip install -r requirements.txt
```

6. Setup Environment Variables
Create a .env file in the root directory and add your credentials.
(Note: You need API keys from Groq, Hugging Face, and Pinecone)
```bash
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
GROQ_API_KEY = "gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
HUGGINGFACEHUB_API_TOKEN = "hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

8. Ingest Data (Create Embeddings)
Run this only once to process your PDFs and store vectors in Pinecone:
```bash
python store_index.py
```

10. Run the Application
```bash
python app.py
```

12. Access the Chatbot
Open your browser and go to:
```bash
http://localhost:8080
```

---

🌐 Deployment (Render)
This project is currently deployed on Render as a Web Service.
Deployment Steps:
 * Push to GitHub: Ensure your latest code (with requirements.txt and Procfile) is on GitHub.
 * Create New Web Service: Log in to Render and connect your GitHub repository.
 * Configure Settings:
   * Runtime: Python 3
   * Build Command: pip install -r requirements.txt
   * Start Command: gunicorn app:app
 * Environment Variables:
   Add the following secrets in the "Environment" tab on Render:
   * PYTHON_VERSION: 3.10.12
   * PINECONE_API_KEY: (Your Key)
   * GROQ_API_KEY: (Your Key)
   * HUGGINGFACEHUB_API_TOKEN: (Your Key)
 * Deploy: Click "Manual Deploy" -> "Clear build cache & deploy" to go live.


---

### 📂 Directory Structure

```text
AI-Bot/
├── Data/                   # PDF files for knowledge base
├── src/
│   ├── helper.py           # Embedding & PDF loading logic
│   ├── prompt.py           # System prompts for Llama-3
├── templates/
│   └── chat.html           # Frontend UI
├── static/
│   └── style.css           # Styling
├── app.py                  # Main Flask application
├── store_index.py          # Script to ingest data into Pinecone
├── requirements.txt        # Project dependencies
├── Procfile                # Deployment command for Render
└── .env                    # API Secrets (Not committed to Git)
```


---

