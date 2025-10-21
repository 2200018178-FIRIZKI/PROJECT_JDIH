from qdrant_client import QdrantClient

COLLECTION_NAME = "pdf_chunks"

client = QdrantClient(host="localhost", port=6333)

# Cek collection
collections = client.get_collections()
print("Collections:", collections)

# Cek jumlah point
count = client.count(collection_name=COLLECTION_NAME)
print(f"Jumlah embedding di collection '{COLLECTION_NAME}':", count)

# Cek beberapa point


points, _ = client.scroll(collection_name=COLLECTION_NAME, limit=5)
print("Contoh data di Qdrant:")
for point in points:
    print(f"id={point.id} vector={point.vector[:5] if point.vector else None} ... payload={point.payload}")

# Cek pencarian vektor (ambil vektor dari salah satu point)
if points and points[0].vector:
    query_vector = points[0].vector
    result = client.query_points(collection_name=COLLECTION_NAME, query_vector=query_vector, limit=3)
    print("Hasil pencarian Qdrant:")
    for hit in result:
        print(hit)
else:
    print("Tidak ada data vector untuk pencarian.")
