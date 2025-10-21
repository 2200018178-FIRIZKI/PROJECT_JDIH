masuk-psql:
    psql -U jdih_user -h localhost -d jdih_db

aktifin-venv:
    .\venv\Scripts\Activate.ps1

install-requirements:
    pip install -r requirements.txt

run-pipeline:
    python utils/postgres_client.py

run-embedding:
    python utils/qdrant_wrapper.py

run-main:
    python src/main.py

docker-up:
    cd docker && docker compose up -d

docker-down:
    cd docker && docker compose down -v

qdrant-check:
    python utils/qdrant_check.py

