# Wrapper PostgreSQL client
import psycopg2

class PostgresClient:
    def __init__(self, dbname, user, password, host='localhost', port=5432):
        self.conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

    def insert_chunk(self, source_file, chunk_text, chunk_index):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO pdf_chunks (source_file, chunk_text, chunk_index)
                VALUES (%s, %s, %s)
            """, (source_file, chunk_text, chunk_index))
            self.conn.commit()

    def fetch_chunks(self, source_file):
        with self.conn.cursor() as cur:
            cur.execute("SELECT chunk_text FROM pdf_chunks WHERE source_file = %s ORDER BY chunk_index", (source_file,))
            return [row[0] for row in cur.fetchall()]
