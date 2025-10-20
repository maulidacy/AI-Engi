from fastapi import FastAPI
from .logging import setup_logging
from .version import __version__

logger = setup_logging()
app = FastAPI(title="Hello-Service", version=__version__)

@app.get("/health")
async def health():
    logger.info("Health check requested")
    return {"status": "healthy"}

@app.get("/version")
async def version():
    logger.info("Version requested")
    return {"version": __version__}
