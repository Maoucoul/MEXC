import asyncio

from mexc.futures import Futures
from mexc.spot import Spot
from config import token, fingerprint, userAgent

ft = Futures(token, fingerprint, userAgent)
st = Spot(token, fingerprint, userAgent)


# via spot -> LIMIT_ORDER or MARKET_ORDER

# futures
# "OPEN_LONG"
# "CLOSE_SHORT"
# "OPEN_SHORT"
# "CLOSE_LONG"
#
# "ISOLATED"
# "CROSS",
#
# "PRICE_LIMITED_ORDER"
# "POST_ONLY_MAKER"
# "TRANSACT_OR_CANCEL_INSTANTLY"
# "TRANSACT_COMPLETELY_OR_CANCEL_COMPLETELY"
# "MARKET_ORDERS"
# "CONVERT_MARKET_PRICE_TO_CURRENT_PRICE"


async def main():
    # LEVERAGE = 200
    # PRICE = "143"
    # VOL = 10
    #
    # params = {
    #     "stopLossPrice": "150",
    #     "takeProfitPrice": "140"
    # }
    # #
    # response_1 = await ft.createOrder(
    #     "SOL_USDT", "OPEN_SHORT", "CROSS",
    #     "PRICE_LIMITED_ORDER", VOL, LEVERAGE, PRICE, **params
    # )
    # print(response_1)
    # #
    # stopLoss = "230"
    # takeProfit = "180"
    #
    # response_2 = await ft.changeOrderSLTP(
    #     response_1['data']['orderId'], stopLoss, takeProfit
    # )
    # print(response_2)
# 
#     params = {
#         "loseTriggerPrice": "40000",
#         "profitTriggerPrice": "80000"
#     }
#     response = await st.buyOrder("BTC_USDT", "50000", "0.000100",
#                                  "LIMIT_ORDER", params)
#     print(response)

    # response = await st.buyOrder("BTC_USDT", "50000", "0.000100", "MARKET_ORDER")
    # print(response)

    # response = await st.sellOrder("BTC_USDT", "60000", "0.000100", "MARKET_ORDER")
    # print(response)


asyncio.run(main())
