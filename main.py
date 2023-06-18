from app.backend.app.router import router
import uvicorn
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

app.include_router(router)

handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
