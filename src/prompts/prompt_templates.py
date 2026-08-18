QA_PROMPT = """Asagidaki baglama dayanarak soruya kisa ve net cevap ver.
Baglamda bilgi yoksa "Bilmiyorum" de.

Baglam:
{context}

Soru: {question}

Cevap:"""

def build_qa_prompt(context: str, question: str) -> str:
    return QA_PROMPT.format(context=context, question=question)
