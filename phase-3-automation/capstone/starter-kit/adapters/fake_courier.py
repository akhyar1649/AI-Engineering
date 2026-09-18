def normalize(payload: dict[str, object]) -> dict[str, object]:
    return {
        "event_id": str(payload["id"]),
        "shipment_id": str(payload["tracking_no"]),
        "status": payload["state"],
        "event_time": payload["occurred_at"],
    }
