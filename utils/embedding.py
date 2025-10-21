# Fungsi embedding dengan model sentence-transformers
from sentence_transformers import SentenceTransformer

def embed_chunks(chunks, model_name='all-MiniLM-L6-v2'):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(chunks)
    # Pastikan hasilnya list of list of float, bukan numpy array
    if hasattr(embeddings, "tolist"):
        embeddings = embeddings.tolist()
    return embeddings
