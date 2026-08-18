import chromadb

from src.utils.helpers import BASE_DIR

class VectorStore:
    def __init__(self, collection: str = "rag_docs"):
        self.client = chromadb.PersistentClient(
            path=str(BASE_DIR / "data" / "chroma"))
        self.collection = self.client.get_or_create_collection(collection)

    def add(self, ids, texts, embeddings, metadatas):
        self.collection.add(ids=ids, embeddings=embeddings,
                            documents=texts, metadatas=metadatas)

    def search(self, embedding: list[float], top_k: int = 5) -> list[dict]:
        res = self.collection.query(query_embeddings=[embedding], n_results=top_k)
        return [{"text": t, "source": m.get("source")}
                for t, m in zip(res["documents"][0], res["metadatas"][0])]
