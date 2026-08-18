# rag-project

Moduler RAG pipeline:
ingestion → chunking → embeddings → vectordb → retrieval → llm → api

## Kurulum
pip install -r requirements.txt
cp .env.example .env   # OPENAI_API_KEY doldur
mkdir -p data          # belgelerini buraya at (.txt, .md, .csv)

## Belgeleri indexle
python main.py ingest

## API'yi calistir
uvicorn src.api.routes:app --reload

## Test
pytest -q
