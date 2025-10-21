
from sqlalchemy import create_engine, Column, Integer, Text, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Chunk(Base):
    __tablename__ = "chunks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(Text)
    source = Column(String)

def save_chunks_to_postgres(chunks, db_url="postgresql://jdih_user:jdih_pass@localhost:5432/jdih_db"):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for chunk in chunks:
        chunk_obj = Chunk(content=chunk.page_content, source=str(chunk.metadata.get("source", "")))
        session.add(chunk_obj)
    session.commit()
    session.close()

if __name__ == "__main__":
    from chunk_pdf import chunk_pdf
    chunks = chunk_pdf("data/view.pdf")  # Path diperbaiki
    save_chunks_to_postgres(chunks)
    print("Chunks berhasil disimpan ke PostgreSQL.")
