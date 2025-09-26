import json
from backend.vector_store import VectorStore
from backend.utils import client


class Recommender:
    def __init__(self, products_path: str):
        with open(products_path, "r", encoding="utf-8") as f:
            products = json.load(f)

        items = [
            {
                "id": p["id"],
                "text": f"{p['name']}. {p['description']}",
                "meta": p
            }
            for p in products
        ]
        self.vs = VectorStore()
        self.vs.build_from_items(items, text_key="text")
        self.products = products

    def recommend(self, query: str, topk: int = 3):
        results = self.vs.query(query, topk=topk)
        print("DEBUG RESULTS:", results)   # 👈 add this
        if not results:
            return {"products": [], "explanation": "No matches found."}

        # Now this will work, since meta has name+description
        context = "\n".join(
            [f"{r['meta']['meta']['name']}: {r['meta']['meta']['description']}" for r in results]
        )


        try:
            completion = client.chat.completions.create(
                model="openai/gpt-oss-20b:nebius",
                messages=[
                    {"role": "system", "content": "You are a helpful sales assistant."},
                    {"role": "user", "content": f"User asked: {query}\nHere are some products:\n{context}\nRecommend the best option and explain why."}
                ],
            )
            explanation = completion.choices[0].message.content.strip()
        except Exception as e:
            print("HF API error:", e)
            explanation = "Could not generate explanation at this time."

        return {
    "products": [r["meta"]["meta"] for r in results],
    "explanation": explanation
}

