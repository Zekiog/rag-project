# rag-project

[![CI](https://github.com/Zekiog/rag-project/actions/workflows/ci.yml/badge.svg)](https://github.com/Zekiog/rag-project/actions/workflows/ci.yml)
![Last commit](https://img.shields.io/github/last-commit/Zekiog/rag-project)

A modular retrieval-augmented generation (RAG) pipeline in Python.

```text
ingestion -> chunking -> embeddings -> vector store -> retrieval -> LLM -> API
```

Each stage lives in its own module under `src/`, so any component (chunker, embedding model, vector store, LLM) can be swapped without touching the rest.

## Quick start

```bash
pip install -r requirements.txt
cp .env.example .env        # set OPENAI_API_KEY
mkdir -p data               # place source documents here (.txt, .md, .csv)
```

## Index documents

```bash
python main.py ingest
```

## Run the API

```bash
uvicorn src.api.routes:app --reload
```

## Run the tests

```bash
pytest -q
```

## Configuration

Runtime settings are read from `config.yaml` and environment variables. Secrets belong in `.env`, which is git-ignored. See `.env.example` for the expected keys.

## Project layout

| Path | Purpose |
|---|---|
| `src/` | Pipeline modules and API routes |
| `tests/` | Unit tests |
| `config.yaml` | Pipeline settings |
| `main.py` | Command-line entry point |

## Security

See [SECURITY.md](SECURITY.md) for how to report a vulnerability.
