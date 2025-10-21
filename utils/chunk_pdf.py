
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_pdf(pdf_path, chunk_size=1000, chunk_overlap=200):
    # Load PDF
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Split text into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = splitter.split_documents(documents)
    return chunks

if __name__ == "__main__":
    pdf_path = "../data/view.pdf"  # Sesuaikan path jika perlu
    chunks = chunk_pdf(pdf_path)
    print(f"Total chunks: {len(chunks)}")
    print("Contoh chunk pertama:\n", chunks[0].page_content)
