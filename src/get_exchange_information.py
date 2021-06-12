import ccxt
from src import keys


def get_exchange_keys():
    return {
        "apiKey": keys.exchange_key,
        "secret": keys.exchange_secret,
        "password": keys.exchange_password,
        "verbose": False,
    }


def get_exchange(exchange_name):
    exchange = getattr(ccxt, exchange_name)(get_exchange_keys())
    if keys.exchange_env != "prod":
        print("setting env to test")
        exchange.urls["api"] = exchange.urls["test"]
    return exchange
