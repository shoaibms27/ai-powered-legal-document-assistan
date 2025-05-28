# LegalEase: AI-Powered Legal Document Assistant

LegalEase is a web-based GenAI tool that allows users to upload a legal document (PDF), ask questions about it in natural language, and get simplified, cited answers using Retrieval-Augmented Generation (RAG).

## Features
- Upload and process legal PDFs
- Ask questions in natural language
- Get simplified, cited answers using RAG
- Uses Google Gemma (via Groq API) as the LLM
- Secure: uploaded files are deleted after session
- No persistent storage of user queries or responses

## Tech Stack
- Python
- Streamlit (UI)
- LangChain (RAG pipeline)
- FAISS (vector store)
- sentence-transformers (embeddings)
- Groq API (LLM)
- PyMuPDF (PDF parsing)
- python-dotenv (secrets)

## Folder Structure
```
legalease/
├── app.py                  # Streamlit UI + RAG pipeline
├── utils/
│   ├── document_loader.py  # PDF loader and text splitter
│   ├── embedder.py         # Embedding logic
│   ├── vector_store.py     # FAISS logic (legacy, not used in final app)
│   └── query_handler.py    # LangChain + Groq + retrieval QA
├── data/
│   └── uploaded_docs/      # Uploaded PDF files (temporary)
├── requirements.txt        # Dependencies
├── .env                    # Store GROQ_API_KEY (not committed)
└── README.md               # Project documentation
```

## Setup Instructions

1. **Clone the repository**
   ```sh
   git clone https://github.com/shoaibms27/ai-powered-legal-document-assistan.git
   cd ai-powered-legal-document-assistan/legalease
   ```

2. **Create and activate a virtual environment (recommended)**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   pip install langchain-groq
   # On Windows, install FAISS manually from https://www.lfd.uci.edu/~gohlke/pythonlibs/#faiss
   ```

4. **Set up your Groq API key**
   - Create a `.env` file in the `legalease/` directory:
     ```
     GROQ_API_KEY=your_actual_groq_api_key_here
     ```

5. **Run the app**
   ```sh
   streamlit run app.py
   ```

6. **Usage**
   - Open the local Streamlit URL in your browser.
   - Upload a PDF, ask questions, and get answers!

## Security & Privacy
- Uploaded files are deleted after session.
- No persistent storage of user queries or answers.
- Uses Streamlit session state for file management.

## Disclaimer
> This is not legal advice; consult a professional.

## License
MIT 