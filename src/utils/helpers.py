import logging
from pathlib import Path

import yaml
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[2]

def load_config(path: str = "config.yaml") -> dict:
    with open(BASE_DIR / path, encoding="utf-8") as f:
        return yaml.safe_load(f)

def setup_logging(log_file: str = "logs/app.log") -> logging.Logger:
    load_dotenv()
    logger = logging.getLogger("rag")
    logger.setLevel(logging.INFO)
    log_path = BASE_DIR / log_file
    log_path.parent.mkdir(parents=True, exist_ok=True)
    fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    if not logger.handlers:
        fh = logging.FileHandler(log_path, encoding="utf-8")
        fh.setFormatter(fmt)
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        logger.addHandler(fh)
        logger.addHandler(sh)
    return logger
