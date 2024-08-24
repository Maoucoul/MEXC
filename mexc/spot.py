from mexc.sign import get_data
from config import coins
import aiohttp


class Spot:
    def __init__(self, token, fingerprint, userAgent):
        self.token = token
        self.fingerprint = fingerprint
        self.userAgent = userAgent

    async def buyOrder(
            self, coin, price, quantity, orderType, params=None
    ):
        if params is None:
            params = {}

        url = ""
        if orderType == "LIMIT_ORDER":
            url = "https://www.mexc.com/api/platform/spot/order/place"

        elif orderType == "MARKET_ORDER":
            url = "https://www.mexc.com/api/platform/spot/v4/order/place"


        data = {
            "currencyId": coins[coin]['currencyId'],
            "marketCurrencyId": coins[coin]['marketCurrencyId'],
            "tradeType": "BUY",
            "price": price,
            "quantity": quantity,
            "orderType": orderType,
        }
        data.update(params)

        data, sign, ts = get_data(self.fingerprint, data, self.token)

        self.userAgent['x-mxc-sign'] = sign
        self.userAgent['x-mxc-nonce'] = ts
        self.userAgent['Authorization'] = self.token

        headers = self.userAgent
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=data) as response:
                return await response.json()

    async def sellOrder(
            self, coin, price, quantity, orderType, params=None
    ):
        if params is None:
            params = {}

        url = ""
        if orderType == "LIMIT_ORDER":
            url = "https://www.mexc.com/api/platform/spot/order/place"

        elif orderType == "MARKET_ORDER":
            url = "https://www.mexc.com/api/platform/spot/v4/order/place"

        data = {
            "currencyId": coins[coin]['currencyId'],
            "marketCurrencyId": coins[coin]['marketCurrencyId'],
            "tradeType": "SELL",
            "price": price,
            "quantity": quantity,
            "orderType": orderType,
        }
        data.update(params)

        data, sign, ts = get_data(self.fingerprint, data, self.token)

        self.userAgent['x-mxc-sign'] = sign
        self.userAgent['x-mxc-nonce'] = ts
        self.userAgent['Authorization'] = self.token

        headers = self.userAgent
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=data) as response:
                return await response.json()



