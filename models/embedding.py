# Konfigurasi dan wrapper model embedding khusus
from qwen_embedding import QwenEmbedding

class EmbeddingModel:
    def __init__(self):
        self.model = QwenEmbedding()

    def embed(self, texts):
        return self.model.encode(texts)
