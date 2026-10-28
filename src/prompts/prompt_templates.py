QA_PROMPT = """Answer the question briefly and clearly using only the context below.
If the context does not contain the answer, reply "I don't know".

Context:
{context}

Question: {question}

Answer:"""

def build_qa_prompt(context: str, question: str) -> str:
    return QA_PROMPT.format(context=context, question=question)
