from fastapi import APIRouter, HTTPException
from src.models import Trade
from src.get_exchange_information import get_exchange
from src import keys

router = APIRouter()


@router.post("/trade/{exchange}")
async def trade(exchange, trade: Trade):
    # exchange can be any of the exchanges supported by ccxt
    # https://github.com/ccxt/ccxt
    # password match for security.
    if keys.api_password == trade.password:
        exchange_instance = get_exchange(exchange)
        # true will close all open opposite ordres
        if trade.close_opposite_orders:
            cancel_orders_response = await cancel_orders(exchange_instance, trade.side)
        else:
            cancel_orders_response = True
        if cancel_orders_response:
            if trade.stop_price is not None and trade.stop is not None:
                # working sample for coinbasepro
                params = {"stopPrice": trade.stop_price, "stop": trade.stop}
            else:
                params = {}
            order_response = exchange_instance.create_order(
                trade.symbol, trade.type, trade.side, trade.size, trade.price, params
            )
            print(f"order_response: {order_response}")
            return {"success": True}
    else:
        raise HTTPException(status_code=401, detail="Unauthorized User")


async def cancel_orders(exchange_instance, side):
    orders = exchange_instance.fetch_open_orders()
    for order in orders:
        if order["info"]["side"] != side:
            exchange_instance.cancel_order(order["id"])
    return True
