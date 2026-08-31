# rag-project


<!-- BADGES-START -->
[![CI](https://github.com/Zekiog/rag-project/actions/workflows/ci.yml/badge.svg)](https://github.com/Zekiog/rag-project/actions/workflows/ci.yml)
![License](https://img.shields.io/github/license/Zekiog/rag-project)
![Last commit](https://img.shields.io/github/last-commit/Zekiog/rag-project)
<!-- BADGES-END -->
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
