import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection(name="documents")

def add_documents(chunks: list[str], embeddings: list[list[float]]) -> None:
    ids = [str (i) for i in range(len(chunks))]
    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids,
    )


def search(query_embedding: list[float], top_k: int = 3) -> list[str]:
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    return results["documents"][0]