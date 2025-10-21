# Project JDIH Chatbot RAG

Struktur project chatbot dengan Retrieval Augmented Generation (RAG), LLM, embedding, chunking, PostgreSQL, Qdrant, dan pemrosesan PDF.

## Struktur Folder
- `src/` : Source code utama
- `data/` : File data (misal PDF)
- `docker/` : Konfigurasi Docker (Qdrant)
- `db/` : Skrip dan konfigurasi database PostgreSQL
- `notebooks/` : Eksplorasi dan prototyping
- `tests/` : Unit dan integrasi test
- `utils/` : Helper dan utilitas
- `docs/` : Dokumentasi
- `models/` : Konfigurasi/model LLM & embedding

## Langkah Utama
1. Chunking PDF dengan LangChain
2. Simpan chunk ke PostgreSQL
3. Embedding chunk ke Qdrant
4. Integrasi LLM untuk chatbot

## Progress Task

| No | Task                                                                 | Status      |
|----|----------------------------------------------------------------------|-------------|
| 1  | Membuat struktur folder dan file project                             | ✅ Selesai  |
| 2  | Upload project ke GitHub                                             | ✅ Selesai  |
| 3  | Instalasi Qdrant VectorDB dengan Docker                              | ✅ Selesai  |
| 4  | Setup database PostgreSQL (Docker & pgAdmin)                         | ✅ Selesai  |
| 5  | Implementasi proses chunking PDF dengan OCR (hasil scan)             | ✅ Selesai  |
| 6  | Simpan hasil chunk ke PostgreSQL                                     | ✅ Selesai  |
| 7  | Cek data chunk di database (psql & pgAdmin)                          | ✅ Selesai  |
| 8  | Embedding chunk menggunakan SentenceTransformer                      | ✅ Selesai  |
| 9  | Simpan embedding ke Qdrant                                           | ✅ Selesai  |
| 10 | Similarity search embedding di Qdrant (Python & Dashboard)           | ✅ Selesai  |
| 11 | Visualisasi dan monitoring data di Qdrant                            | ✅ Selesai  |
| 12 | Integrasi Qdrant dengan LLM Chatbot                                  | ❌ Belum    |
| 13 | Implementasi pipeline RAG                                            | ❌ Belum    |
| 14 | Unit test dan integrasi test                                         | ❌ Belum    |
| 15 | Dokumentasi penggunaan dan instalasi                                 | ❌ Belum    |

## Requirements
Lihat `requirements.txt` untuk dependensi utama.
