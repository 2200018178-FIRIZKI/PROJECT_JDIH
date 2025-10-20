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

## Requirements
Lihat `requirements.txt` untuk dependensi utama.
