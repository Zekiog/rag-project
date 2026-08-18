def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    words = text.split()
    chunks, start = [], 0
    while start < len(words):
        chunks.append(" ".join(words[start:start + chunk_size]))
        start += chunk_size - overlap
    return chunks

def chunk_documents(docs: list[dict], chunk_size: int = 500,
                    overlap: int = 50) -> list[dict]:
    chunks = []
    for doc in docs:
        for i, c in enumerate(chunk_text(doc["text"], chunk_size, overlap)):
            chunks.append({"chunk_id": f"{doc['source']}#{i}",
                           "source": doc["source"],
                           "text": c})
    return chunks
