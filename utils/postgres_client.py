
from sqlalchemy import create_engine, Column, Integer, Text, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Chunk(Base):
    __tablename__ = "pdf_chunks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    source_file = Column(String(255))
    chunk_text = Column(Text)
    chunk_index = Column(Integer)
    created_at = Column(String, default=None)  # DB akan mengisi otomatis

def save_chunks_to_postgres(chunks, db_url="postgresql://jdih_user:jdih_pass@localhost:5432/jdih_db"):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for idx, chunk in enumerate(chunks):
        chunk_obj = Chunk(
            source_file="data/view.pdf",
            chunk_text=chunk,
            chunk_index=idx
        )
        session.add(chunk_obj)
    session.commit()
    session.close()

if __name__ == "__main__":
    from chunk_pdf import chunk_pdf_ocr
    chunks = chunk_pdf_ocr("data/view.pdf")
    print(f"Jumlah chunk yang dihasilkan: {len(chunks)}")
    if len(chunks) > 0:
        print("Contoh chunk:", chunks[0])
    else:
        print("Tidak ada chunk yang dihasilkan dari PDF!")
    save_chunks_to_postgres(chunks)
    print("Chunks berhasil disimpan ke PostgreSQL.")
