from pathlib import Path

from src.utils.helpers import BASE_DIR

SUPPORTED = {".txt", ".md", ".csv"}

def load_documents(data_dir: str = "data") -> list[dict]:
    docs = []
    root = BASE_DIR / data_dir
    if not root.exists():
        return docs
    for path in sorted(root.rglob("*")):
        if path.suffix.lower() in SUPPORTED:
            docs.append({"source": str(path.relative_to(BASE_DIR)),
                         "text": path.read_text(encoding="utf-8")})
    return docs
