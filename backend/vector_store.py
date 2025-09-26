from sentence_transformers import SentenceTransformer
import faiss

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"  # free, fast, accurate

class VectorStore:
    def __init__(self, dim=384, model_name=MODEL_NAME):
        self.model = SentenceTransformer(model_name)
        self.index = faiss.IndexFlatIP(dim)
        self.items = []

    def _embed(self, texts):
        return self.model.encode(texts, convert_to_numpy=True, normalize_embeddings=True)

    def build_from_items(self, items, text_key="text"):
        embeddings = self._embed([item[text_key] for item in items])
        self.index.add(embeddings)
        self.items = items

    def query(self, query_text, topk=5):
        q_emb = self._embed([query_text])
        scores, ids = self.index.search(q_emb, topk)
        return [
            {"score": float(s), "meta": self.items[i]}
            for s, i in zip(scores[0], ids[0])
            if i != -1
        ]
