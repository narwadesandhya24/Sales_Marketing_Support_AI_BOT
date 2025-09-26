import csv
from backend.vector_store import VectorStore
from backend.utils import client

class SupportBot:
    def __init__(self, faq_csv_path: str):
        items = []
        with open(faq_csv_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                items.append({"text": row["question"], "answer": row["answer"]})
        self.vs = VectorStore()
        self.vs.build_from_items(items, text_key="text")

    def answer(self, query: str, topk=3):
        results = self.vs.query(query, topk=topk)
        if not results:
            return self._llm_fallback(query)

        best = results[0]
        if best["score"] < 0.4:
            return self._llm_fallback(query)

        return {"answer": best["meta"]["answer"], "escalate": False}

    def _llm_fallback(self, query: str):
        completion = client.chat.completions.create(
            model="openai/gpt-oss-20b:nebius",
            messages=[
                {"role": "system", "content": "You are a helpful customer support assistant."},
                {"role": "user", "content": query}
            ],
        )
        return {
            "answer": completion.choices[0].message.content.strip(),
            "escalate": False
        }
