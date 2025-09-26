#  AI-Powered Sales, Marketing & Support Assistant

This project is an **end-to-end AI platform** that automates three core business functions:

-  **Sales Recommender** → Suggests the most relevant products to customers using semantic search + LLM explanations.  
-  **Social Media Creator** → Generates marketing captions and campaign ideas.  
-  **Support Bot** → Answers FAQs or falls back to AI when no FAQ is found.  

Built with **FastAPI + Streamlit**, powered by **Sentence Transformers, FAISS, and Hugging Face-hosted LLMs**.

---

##  Features
- **Unified Assistant** → Sales, Marketing, and Support in one interface.  
- **Semantic Search** → Uses [Sentence Transformers](https://www.sbert.net/) for query embeddings.  
- **Vector Database** → FAISS for fast similarity search.  
- **Generative AI** → Hugging Face LLMs (via OpenAI client) for explanations & creative content.  
- **Streamlit Frontend** → Easy-to-use web app interface.  
- **Fallback Support** → Ensures customers always get an answer.  

---

##  Architecture

Frontend (Streamlit)  --->  Backend (FastAPI)
         |                         |
         |                         +--> Recommender (SBERT + FAISS + LLM)
         |                         +--> Social Media (LLM)
         |                         +--> Support Bot (FAQ + FAISS + LLM fallback)
         |
   Hugging Face API  <-------------+

---


##  Setup Instructions

### 1. Clone Repo
```bash
git clone https://github.com/narwadesandhya24/Sales_Marketing_Support_AI_BOT
```

### 2. Create Virtual Environment
```bash
python -m venv venv

source venv/bin/activate   # (Linux/macOS)

venv\Scripts\activate      # (Windows)
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add Environment Variables
Create a `.env` file in the project root:
```
HF_TOKEN=<your_huggingface_api_token>

```

---

##  Running the Project

### Start Backend (FastAPI)
```bash
python -m uvicorn backend.main:app --reload
```

Backend will be live at:  
 http://127.0.0.1:8000  
 Swagger docs: http://127.0.0.1:8000/docs  

### Start Frontend (Streamlit)
```bash
streamlit run app/streamlit_app.py
```

Streamlit UI will be live at:  
 http://localhost:8501  

---

##  Example Queries

### Sales Recommender
```json
{ "text": "I need a tool for task management and collaboration." }
```
→ Returns **Acme Productivity Suite** with explanation.

### Social Media
```json
{ "prompt": "Generate 3 captions for a coffee shop launch" }
```
→ Returns 3 creative social captions.

### Support Bot
```json
{ "query": "How do I reset my password?" }
```
→ Returns matching FAQ or AI-generated response.

---

##  Tech Stack
- **Frontend**: Streamlit  
- **Backend**: FastAPI + Uvicorn  
- **Embeddings**: Sentence Transformers (`all-MiniLM-L6-v2`)  
- **Vector DB**: FAISS  
- **LLM API**: Hugging Face Router (via OpenAI client)  
- **Secrets**: `.env`  

---

##  Future Improvements
- Analytics dashboard (usage stats, success rate).  
- Multi-turn conversations in Support Bot.  
- Personalization of recommendations.  
- Dockerized deployment for cloud use.