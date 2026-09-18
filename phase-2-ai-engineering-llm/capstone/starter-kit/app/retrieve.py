def retrieve(query: str, documents: list[dict[str, str]]) -> list[dict[str, str]]:
    terms = set(query.lower().split())
    return sorted(documents, key=lambda doc: len(terms & set(doc["text"].lower().split())), reverse=True)[:3]
