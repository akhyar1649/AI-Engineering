from fastapi import FastAPI

app = FastAPI(title="Kirimin Support Intelligence")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
