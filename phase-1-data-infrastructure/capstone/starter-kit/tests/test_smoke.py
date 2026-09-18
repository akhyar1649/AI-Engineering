from kirimin_pipeline.generate import generate_orders


def test_generator_is_reproducible() -> None:
    assert generate_orders(3, seed=42) == generate_orders(3, seed=42)
