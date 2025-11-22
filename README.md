# VectorDB – Hands-on Vector Database with PDF RAG Pipeline

A complete, beginner-friendly project to learn **vector databases**, **text embeddings**, **semantic search**, and **Retrieval-Augmented Generation (RAG)** using real-world PDF documents.

This project walks you through the entire pipeline:
1. Extract text from PDFs (including scanned/image-based PDFs)
2. Generate high-quality embeddings
3. Store and index vectors locally
4. Perform semantic search over your documents
5. Enable question answering using retrieved context (RAG-ready)

Perfect for learning RAG, building document AI apps, or preparing for LLM interviews!

## Features

- PDF text extraction (supports scanned PDFs via Tesseract OCR)
- Smart text chunking and cleaning
- Embedding generation using Sentence Transformers
- Local vector storage & fast similarity search (FAISS)
- Query → Embedding → Semantic Search pipeline
- Interactive Q&A over your private documents
- Fully containerized with Docker (no local setup needed!)
- Easy to extend: Chroma, Pinecone, Weaviate, Qdrant, etc.

## Project Structure

```bash
VECTORDB/
├── PyTesseract/                  # OCR-enabled Python environment
│   ├── Dockerfile
│   └── requirements.txt
│
├── PythonScript/
│   ├── main.py                   # Main entry point
│   ├── module/
│   │   ├── PdfProcessModule.py   # PDF → clean text extraction
│   │   ├── Query2Quant.py        # Convert query to vector
│   │   ├── VectToQuant.py        # Document → embeddings + indexing
│   │   └── __pycache__/
│   └── PDFs/                     # Drop your PDFs here
│       └── dummy.pdf
│
├── docker-compose.yml

A simple, local vector database application that lets you ask natural language questions about your PDF documents.  
It uses:
- **PyPDF2 + pdf2image + Tesseract OCR** to extract text (including scanned PDFs)
- **Sentence Transformers** to generate embeddings
- **FAISS** for fast similarity search
- Pure Python, no external APIs or internet required

Perfect for searching contracts, notices, invoices, or any personal/document archive.

## Features
- Handles both digital and scanned PDFs
- Builds a persistent FAISS index (reuses embeddings on subsequent runs)
- Interactive question-answering prompt
- Fully offline & private


## Quick Start (Docker)

```bash
# Build and start the service
docker compose build
docker compose up

# The app will automatically:
# - Extract text from PDFs
# - Generate embeddings
# - Build FAISS index
# - Launch interactive semantic search

# Enter the running container
docker exec -it ocr-service bash

# Inside the container, run:
cd /PythonScript
python main.py