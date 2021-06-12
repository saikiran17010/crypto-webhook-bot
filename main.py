from fastapi import FastAPI
from src import webhook
from mangum import Mangum

app = FastAPI(
    title="Crypto Webhook trading",
    description="Automated trading from tradingview webhooks",
    version="0.0.1",
)

app.include_router(webhook.router)

handler = Mangum(app)
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
