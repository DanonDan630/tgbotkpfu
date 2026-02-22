import uvicorn
from app.api import api_app
from app.services.csv_cache import ensure_startup_cache
import asyncio

if __name__ == "__main__":
    asyncio.run(ensure_startup_cache())
    uvicorn.run(api_app, host="127.0.0.1", port=5000)