# crypto-webhook-bot

webhook to trigger crypto trading orders from tradingview and other supported platforms

# Installation

git clone git@github.com:algobots-net/crypto-webhook-bot.git
cd crypto-webhook-bot

# Testing in local environment

```python
python3 -m venv venv
source venv/bin/activate # for linux/macos
source venv/Scripts/activate # for windows
pip install -r requirements.txt
uvicorn main:app --reload --port 80
```

# Testing in docker environment

```docker
docker build -t crypto-webhook-bot .
docker stop crypto-webhook-bot
docker rm crypto-webhook-bot
docker run -it -d --name  crypto-webhook-bot -p 80:80 crypto-webhook-bot
```

- Visit http://localhost/docs for swagger ui
