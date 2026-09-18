"""Quality rule contract for the starter kit."""


def validate(rows: list[dict[str, object]]) -> dict[str, object]:
    return {"input_rows": len(rows), "passed": True, "failures": []}
