import streamlit as st
import os
import tempfile
from utils.document_loader import load_pdf, split_text
from utils.embedder import Embedder
from utils.query_handler import get_qa_chain
from dotenv import load_dotenv
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

st.set_page_config(page_title="LegalEase: AI-Powered Legal Document Assistant")
st.title("LegalEase: AI-Powered Legal Document Assistant")

load_dotenv()

if 'vectorstore' not in st.session_state:
    st.session_state['vectorstore'] = None
if 'texts' not in st.session_state:
    st.session_state['texts'] = []

uploaded_file = st.file_uploader("Upload a legal document (PDF)", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf", dir="legalease/data/uploaded_docs") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name
    text = load_pdf(tmp_path)
    chunks = split_text(text)
    st.session_state['texts'] = chunks
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_texts(chunks, embedding_model)
    st.session_state['vectorstore'] = vectorstore
    os.remove(tmp_path)
    st.success("Document processed and indexed!")

if st.session_state['vectorstore']:
    query = st.text_input("Ask a question about the document:")
    if query:
        retriever = st.session_state['vectorstore'].as_retriever(search_kwargs={"k": 5})
        qa_chain = get_qa_chain(retriever)
        answer = qa_chain.run(query)
        st.markdown(f"**Answer:** {answer}")
        st.markdown("---")
        st.markdown("**Sources:**")
        # Show the top 5 chunks as sources
        docs = st.session_state['vectorstore'].similarity_search(query, k=5)
        for i, doc in enumerate(docs):
            st.markdown(f"**Chunk {i+1}**:\n{doc.page_content[:300]}...")
        st.info("This is not legal advice; consult a professional.") 