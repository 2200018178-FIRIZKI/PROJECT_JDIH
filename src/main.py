# Entry point untuk pipeline RAG chatbot
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.chunk_pdf import chunk_pdf_ocr
from utils.embedding import embed_chunks
from utils.qdrant_wrapper import QdrantClientWrapper
from utils.postgres_client import save_chunks_to_postgres
from models.llm import LLMModel
from models.embedding import EmbeddingModel

# ...existing code...
