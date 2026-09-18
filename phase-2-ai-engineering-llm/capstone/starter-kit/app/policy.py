def route(category: str) -> str:
    if category in {"refund", "account_specific", "pii"}:
        return "human_review"
    return "automated_rag"
