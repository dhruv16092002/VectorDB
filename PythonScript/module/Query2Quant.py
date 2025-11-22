from qdrant_client import QdrantClient
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

class PDFVectorSearch:
    def __init__(self, url: str, collection_name: str, model: str):
        self.collection_name = collection_name
        self.client = QdrantClient(url=url)
        self.embed_model = HuggingFaceEmbedding(model_name=model)

    def embed_text(self, text: str):
        return self.embed_model.get_text_embedding(text)

    def query(self, text: str, limit: int = 1):
        vector = self.embed_text(text)

        result = self.client.query_points(
            collection_name=self.collection_name,
            query=vector,
            limit=limit,
            with_payload=True,
            with_vectors=False
        )
        return result

    def results_to_json(self, result):
        output = []
        print("====================")
        print(result)
        print("====================")
        for hit in result.points:
            output.append({
                "id": hit.id,
                "score": hit.score,
                "filename": hit.payload.get("filename"),
                "chunk": hit.payload.get("chunk")
            })

        return output
