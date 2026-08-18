from fastapi.testclient import TestClient

from src.api.routes import app
from src.chunking.chunker import chunk_text

def test_chunk_text():
    text = " ".join(f"w{i}" for i in range(200))
    chunks = chunk_text(text, chunk_size=50, overlap=10)
    assert len(chunks) > 1
    assert all(c.strip() for c in chunks)

def test_health():
    res = TestClient(app).get("/health")
    assert res.status_code == 200
