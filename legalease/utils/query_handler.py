import os
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

def get_groq_llm():
    api_key = os.getenv('GROQ_API_KEY')
    return ChatGroq(
        model="gemma2-9b-it",
        api_key=api_key
    )

def get_qa_chain(retriever):
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=(
            "You are LegalEase, an AI legal document assistant. "
            "Given the following context from a legal document, answer the user's question in simple language. "
            "Cite the relevant sections.\n\nContext:\n{context}\n\nQuestion: {question}\n\nAnswer (with citations):"
        )
    )
    llm = get_groq_llm()
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt}
    ) 