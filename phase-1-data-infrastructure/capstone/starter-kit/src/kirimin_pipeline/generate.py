"""Generate synthetic, intentionally imperfect Kirimin data."""

from __future__ import annotations

import random


def generate_orders(rows: int, seed: int = 42) -> list[dict[str, object]]:
    rng = random.Random(seed)
    cities = ["Jakarta", "JKT", "jakarta", "Bandung", "Surabaya"]
    result: list[dict[str, object]] = []
    for index in range(rows):
        result.append(
            {
                "order_id": f"O-{index:08d}",
                "origin_city": rng.choice(cities),
                "order_value_idr": rng.randint(50_000, 1_500_000),
                "payment_status": rng.choice(["paid", "paid", "pending"]),
            }
        )
    return result
