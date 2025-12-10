from typing import List
from sentence_transformers import SentenceTransformer

# Initialize the embedding model (this will download the model the first time)
# For production, consider a more robust way to manage model loading and caching.
try:
    embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
except Exception as e:
    print(f"Warning: Could not load SentenceTransformer model. Embedding generation will be mocked. Error: {e}")
    embedding_model = None

def generate_embeddings(texts: List[str]) -> List[List[float]]:
    """
    Generates embeddings for a list of text documents.
    """
    if embedding_model:
        embeddings = embedding_model.encode(texts, convert_to_numpy=True).tolist()
        return embeddings
    else:
        # Mock embedding generation if model failed to load
        # In a real scenario, this should be handled more gracefully, e.g., raising an error
        print("Warning: Using mock embeddings because SentenceTransformer model is not loaded.")
        return [[0.0] * 384 for _ in texts] # all-MiniLM-L6-v2 produces 384-dim embeddings
