# Fungsi embedding dengan model khusus (misal Qwen embedding)
from qwen_embedding import QwenEmbedding

def embed_chunks(chunks):
    model = QwenEmbedding()
    embeddings = model.encode(chunks)
    return embeddings
