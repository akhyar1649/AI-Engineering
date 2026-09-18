def build_manifest(documents: list[dict[str, str]]) -> list[dict[str, str]]:
    return [{**doc, "status": "indexed"} for doc in documents]
