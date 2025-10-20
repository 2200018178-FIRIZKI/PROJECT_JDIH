# Wrapper Qdrant client
from qdrant_client import QdrantClient

class QdrantClientWrapper:
    def __init__(self, host='localhost', port=6333):
        self.client = QdrantClient(host=host, port=port)

    def upsert_embeddings(self, collection_name, embeddings, payloads):
        self.client.upsert(collection_name=collection_name, points=embeddings, payload=payloads)

    def search(self, collection_name, query_vector, top_k=5):
        return self.client.search(collection_name=collection_name, query_vector=query_vector, limit=top_k)
