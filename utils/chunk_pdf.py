# Fungsi chunking PDF dengan LangChain
from langchain.text_splitter import CharacterTextSplitter
import pdfplumber

def chunk_pdf(pdf_path, chunk_size=1000, chunk_overlap=100):
    with pdfplumber.open(pdf_path) as pdf:
        text = "\n".join(page.extract_text() or "" for page in pdf.pages)
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = splitter.split_text(text)
    return chunks
