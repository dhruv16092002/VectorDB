from module.PdfProcessModule import *
from module.VectToQuant import *
from module.Query2Quant import *

if __name__ == "__main__":
    # Global Variables
    pdf_path = '/PythonScript/PDFs/BM-Notice-12.11.2025.pdf'
    collection_name = "pdf_embeddings"
    db_url = "http://qdrant:6333"
    model_name = "sentence-transformers/all-MiniLM-L6-v2"

    # PDF reader
    processor = ProcessModule(file_path=pdf_path)
    full_text = processor.ReadPDF()

    # Text to Vector DB
    vdb = Vect2Quant(collection_name=collection_name, db_url=db_url, model=model_name)
    print(
        vdb.insert_pdf(
            filename=Path(pdf_path).name,
            full_text=full_text
        )
    )

    # Query to your VectorDB
    Query = "Your Text Here"

    query_vector_obj = PDFVectorSearch(collection_name=collection_name, url=db_url, model=model_name)

    result = query_vector_obj.query(Query, limit=1)
    output = query_vector_obj.results_to_json(result)
    print(output)

