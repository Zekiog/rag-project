class Retriever:
    def __init__(self, embedder, store, top_k: int = 5):
        self.embedder = embedder
        self.store = store
        self.top_k = top_k

    def retrieve(self, query: str) -> list[dict]:
        embedding = self.embedder.embed([query])[0]
        return self.store.search(embedding, top_k=self.top_k)
