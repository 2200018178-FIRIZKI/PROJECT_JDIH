-- Skrip inisialisasi PostgreSQL untuk menyimpan chunk
CREATE TABLE IF NOT EXISTS pdf_chunks (
    id SERIAL PRIMARY KEY,
    source_file VARCHAR(255),
    chunk_text TEXT,
    chunk_index INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
