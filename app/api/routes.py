from fastapi import APIRouter
from pydantic import BaseModel

from app.embeddings import get_embedding
from app.llm import ask_llm
from app.schemas.api import UploadRequest, AskRequest
from app.vector_store import add_documents, search

router = APIRouter(prefix="")


@router.post("/upload")
def upload(request: UploadRequest) -> dict:
    chunks = [request.text[i:i+500] for i in range(0, len(request.text), 500)]
    embeddings = [get_embedding(chunk) for chunk in chunks]
    add_documents(chunks, embeddings)
    return {"status": "ok", "chunks_count": len(chunks)}

@router.post("/ask")
def ask(request: AskRequest) -> dict:
    query_embedding = get_embedding(request.question)
    context = search(query_embedding)
    answer = ask_llm(request.question, context)
    return {"answer": answer}