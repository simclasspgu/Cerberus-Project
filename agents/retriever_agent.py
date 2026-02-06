class RetrieverAgent:
    def __init__(self, chunks):
        self.chunks = chunks

    def retrieve(self, query, top_k=2):
        # ساده‌ترین retrieval: برگرداندن اولین top_k chunk
        return self.chunks[:top_k]
