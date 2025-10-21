import numpy as np
from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct, Distance, VectorParams

class QdrantClientWrapper:
    def __init__(self, host='localhost', port=6333):
        self.client = QdrantClient(host=host, port=port)

    def create_collection(self, collection_name, vector_size):
        if self.client.collection_exists(collection_name):
            self.client.delete_collection(collection_name)
        self.client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
        )

    def upsert_embeddings(self, collection_name, embeddings, metadatas):
        # Log tipe dan contoh embedding
        print("Tipe embeddings:", type(embeddings))
        if embeddings:
            print("Tipe satu embedding:", type(embeddings[0]))
            print("Contoh embedding (5 dimensi pertama):", embeddings[0][:5])
        # Pastikan embeddings adalah list of float dan tidak None
        points = []
        for emb, meta in zip(embeddings, metadatas):
            if emb is None:
                continue
            if isinstance(emb, np.ndarray):
                emb = emb.tolist()
            elif not isinstance(emb, list):
                emb = list(emb)
            points.append(
                PointStruct(
                    id=meta['id'],
                    vector=emb,
                    payload=meta
                )
            )
        print(f"Upserting {len(points)} embeddings ke Qdrant...")
        try:
            self.client.upsert(collection_name=collection_name, points=points)
        except Exception as e:
            print("Qdrant upsert error:", e)

    def search(self, collection_name, query_vector, top_k=5):
        return self.client.search(collection_name=collection_name, query_vector=query_vector, limit=top_k)

# Contoh pipeline simpan embedding dari chunk
if __name__ == "__main__":
    import sys, os
    from sqlalchemy import create_engine, text
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from utils.embedding import embed_chunks

    # Ambil chunk dari database
    engine = create_engine("postgresql://jdih_user:jdih_pass@localhost:5432/jdih_db")
    with engine.connect() as conn:
        result = conn.execute(text("SELECT id, chunk_text, source_file FROM pdf_chunks"))
        chunks = [(row[0], row[1], row[2]) for row in result]

    chunk_texts = [text for _, text, _ in chunks]
    metadatas = [
        {"id": id, "source_file": source_file, "chunk_text": text}
        for id, text, source_file in chunks
    ]

    # Embedding
    embeddings = embed_chunks(chunk_texts)

    # Simpan ke Qdrant
    qdrant = QdrantClientWrapper()
    # Hapus collection jika sudah ada agar vector tidak None
    if qdrant.client.collection_exists("pdf_chunks"):
        print("Collection pdf_chunks sudah ada, menghapus...")
        qdrant.client.delete_collection("pdf_chunks")
    vector_dim = len(embeddings[0])
    print(f"Membuat collection pdf_chunks dengan dimensi vector: {vector_dim}")
    qdrant.create_collection("pdf_chunks", vector_size=vector_dim)
    qdrant.upsert_embeddings("pdf_chunks", embeddings, metadatas)
    print("Selesai upsert embedding ke Qdrant!")

    # Test upsert manual satu data dengan HTTP client
    print("Test upsert satu data vector manual dengan QdrantClient...")
    try:
        from qdrant_client import QdrantClient
        from qdrant_client.http.models import PointStruct
        http_client = QdrantClient(host="localhost", port=6333)
        test_vector = [float(i) for i in range(vector_dim)]
        test_payload = {"id": 999, "source_file": "test.pdf", "chunk_text": "test chunk"}
        test_point = PointStruct(id=999, vector=test_vector, payload=test_payload)
        http_client.upsert(collection_name="pdf_chunks", points=[test_point])
        print("Upsert manual dengan QdrantClient berhasil!")
        points, _ = http_client.scroll(collection_name="pdf_chunks", limit=1, offset=len(metadatas))
        print("Hasil test scroll point terakhir:", points[0])
    except Exception as e:
        print(f"Gagal upsert/scroll manual dengan QdrantClient: {e}")

    # Test similarity search dari Qdrant
    print("\nTest similarity search di Qdrant (query_points)...")
    print("Signature query_points:")
    print(http_client.query_points.__doc__)
    try:
        query_vector = embeddings[0]
        search_result = http_client.query_points(
            collection_name="pdf_chunks",
            query=query_vector,
            limit=3
        )
        print("Hasil similarity search:")
        for point in search_result[0]:
            print(f"ID: {point.id}, Score: {point.score}, Payload: {point.payload}")
    except Exception as e:
        print(f"Gagal similarity search: {e}")
