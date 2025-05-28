import faiss
import numpy as np
from typing import List, Tuple

class FAISSVectorStore:
    def __init__(self, dim: int):
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []

    def add(self, embeddings: List[List[float]], texts: List[str]):
        arr = np.array(embeddings).astype('float32')
        self.index.add(arr)
        self.texts.extend(texts)

    def search(self, query_embedding: List[float], top_k: int = 5) -> List[Tuple[str, float]]:
        arr = np.array([query_embedding]).astype('float32')
        D, I = self.index.search(arr, top_k)
        results = []
        for idx, dist in zip(I[0], D[0]):
            if idx < len(self.texts):
                results.append((self.texts[idx], dist))
        return results 