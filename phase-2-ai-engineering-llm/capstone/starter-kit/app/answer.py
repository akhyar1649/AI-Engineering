from .policy import route
from .retrieve import retrieve


def answer(query: str, documents: list[dict[str, str]], category: str = "faq") -> dict[str, object]:
    if route(category) == "human_review":
        return {"answer": None, "citations": [], "needs_human": True, "reason_code": "policy_boundary"}
    found = retrieve(query, documents)
    if not found:
        return {"answer": None, "citations": [], "needs_human": True, "reason_code": "no_evidence"}
    return {"answer": found[0]["text"], "citations":[found[0]["id"]], "needs_human":False, "reason_code":None}
