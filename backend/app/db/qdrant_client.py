from typing import List, Dict, Any
from qdrant_client import QdrantClient, models
from backend.app.core.config import settings
from backend.app.core.vector_store import generate_embeddings

# Initialize Qdrant client
qdrant_client = QdrantClient(host=settings.QDRANT_URL) # Use settings.QDRANT_URL

COLLECTION_NAME = "book_content_embeddings"
VECTOR_SIZE = 384 # Size of 'all-MiniLM-L6-v2' embeddings

def create_collection_if_not_exists():
    collections = qdrant_client.get_collections().collections
    if not any(c.name == COLLECTION_NAME for c in collections):
        qdrant_client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=models.VectorParams(size=VECTOR_SIZE, distance=models.Distance.COSINE),
        )
        print(f"Qdrant collection '{COLLECTION_NAME}' created.")
    else:
        print(f"Qdrant collection '{COLLECTION_NAME}' already exists.")

def upsert_vectors(
    texts: List[str], 
    metadatas: Optional[List[Dict[str, Any]]] = None,
    ids: Optional[List[int]] = None
):
    """
    Generates embeddings for texts and upserts them into Qdrant.
    """
    if not texts:
        return

    embeddings = generate_embeddings(texts)
    
    points = []
    for i, emb in enumerate(embeddings):
        payload = metadatas[i] if metadatas and i < len(metadatas) else {}
        point_id = ids[i] if ids and i < len(ids) else None # Allow custom IDs or let Qdrant assign
        
        points.append(
            models.PointStruct(
                id=point_id,
                vector=emb,
                payload=payload
            )
        )

    qdrant_client.upsert(
        collection_name=COLLECTION_NAME,
        wait=True,
        points=points,
    )
    print(f"Upserted {len(points)} vectors into '{COLLECTION_NAME}'.")

def search_vectors(query_text: str, limit: int = 5) -> List[Dict[str, Any]]:
    """
    Searches Qdrant for vectors similar to the query text.
    """
    query_embedding = generate_embeddings([query_text])[0]
    search_result = qdrant_client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_embedding,
        limit=limit
    )
    return [{"payload": hit.payload, "score": hit.score} for hit in search_result]
