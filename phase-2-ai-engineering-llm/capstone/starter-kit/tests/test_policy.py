from app.policy import route


def test_refund_requires_human() -> None:
    assert route("refund") == "human_review"
