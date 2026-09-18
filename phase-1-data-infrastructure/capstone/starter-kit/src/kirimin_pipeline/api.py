"""Minimal API boundary; connect it to the student's serving layer."""

from fastapi import FastAPI

app = FastAPI(title="Kirimin Data Platform")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
