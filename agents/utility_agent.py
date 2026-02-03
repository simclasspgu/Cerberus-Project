
class UtilityAgent:
    def summarize(self, chunks):
        texts = [chunk.text for chunk in chunks]
        return "\n".join(texts[:2])