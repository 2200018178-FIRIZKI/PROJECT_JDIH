# Konfigurasi dan wrapper model embedding khusus
from sentence_transformers import SentenceTransformer

class EmbeddingModel:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

    def embed(self, texts):
        embeddings = self.model.encode(texts)
        if hasattr(embeddings, "tolist"):
            embeddings = embeddings.tolist()
        return embeddings
