import fitz  # PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List


def load_pdf(file_path: str) -> str:
    """
    Load a PDF file and return its full text content.
    """
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text


def split_text(text: str, chunk_size: int = 1000, chunk_overlap: int = 200) -> List[str]:
    """
    Split text into chunks using LangChain's RecursiveCharacterTextSplitter.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_text(text) 
 