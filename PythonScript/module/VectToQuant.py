from pathlib import Path
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
import uuid
import textwrap
from module.PdfProcessModule import ProcessModule
from llama_index.embeddings.huggingface import HuggingFaceEmbedding


class Vect2Quant:
    def __init__(self, db_url: str, collection_name: str, model: str):
        self.client = QdrantClient(url=db_url)
        self.collection_name = collection_name

        self.embed_model = HuggingFaceEmbedding(model_name=model)
        self.vector_size = 384

        if not self.client.collection_exists(self.collection_name):
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(size=self.vector_size, distance=Distance.COSINE)
            )

    def embed_sentence(self, text):
        """Vector embedding using LlamaIndex model"""
        return self.embed_model.get_text_embedding(text)

    def insert_pdf(self, filename, full_text):
        chunks = textwrap.wrap(full_text, 700, break_long_words=False)

        print(f"Total Chunks: {len(chunks)}")

        for chunk in chunks:
            vector = self.embed_sentence(chunk)
            point_id = uuid.uuid4().hex

            self.client.upsert(
                collection_name=self.collection_name,
                points=[
                    PointStruct(
                        id=point_id,
                        vector=vector,
                        payload={
                            "filename": filename,
                            "chunk": chunk
                        }
                    )
                ]
            )

        return "PDF Inserted Successfully"


if __name__ == "__main__":
    pdf_path = '/PythonScript/PDFs/BM-Notice-12.11.2025.pdf'
    collection_name = "pdf_embeddings"
    db_url = "http://qdrant:6333"
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    
    processor = ProcessModule(file_path=pdf_path)
    full_text = processor.ReadPDF()

    vdb = Vect2Quant(db_url, collection_name, model_name)
    print(
        vdb.insert_pdf(
            filename=Path(pdf_path).name,
            full_text=full_text
        )
    )
