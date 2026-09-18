from adapters.fake_courier import normalize


def test_normalize_courier_payload() -> None:
    assert normalize({"id": "E-1", "tracking_no": "S-1", "state": "delivered", "occurred_at": "2026-09-18"})["shipment_id"] == "S-1"
