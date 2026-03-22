import chromadb
from typing import Optional

client = chromadb.Client()
collection = client.get_or_create_collection("career_agent_memory")


def save_user_memory(user_id: str, text: str) -> None:
    try:
        existing = collection.get(ids=[user_id])
        if existing and existing.get("ids"):
            collection.update(ids=[user_id], documents=[text])
        else:
            collection.add(ids=[user_id], documents=[text])
    except Exception:
        collection.add(ids=[user_id], documents=[text])


def get_user_memory(user_id: str) -> Optional[str]:
    try:
        result = collection.get(ids=[user_id])
        docs = result.get("documents", [])
        if docs:
            return docs[0]
    except Exception:
        return None
    return None