from mexc.sign import get_data
import aiohttp

info = {
    "OPEN_LONG": 1,
    "CLOSE_SHORT": 2,
    "OPEN_SHORT": 3,
    "CLOSE_LONG": 4,

    "ISOLATED": 1,
    "CROSS": 2,

    "PRICE_LIMITED_ORDER": 1,
    "POST_ONLY_MAKER": 2,
    "TRANSACT_OR_CANCEL_INSTANTLY": 3,
    "TRANSACT_COMPLETELY_OR_CANCEL_COMPLETELY": 4,
    "MARKET_ORDERS": 5,
    "CONVERT_MARKET_PRICE_TO_CURRENT_PRICE": 6,
}


class Futures:
    def __init__(self, token, fingerprint, userAgent):
        self.token = token
        self.fingerprint = fingerprint
        self.userAgent = userAgent

    async def createOrder(
            self, symbol: str, side: str, openType: str, type: str, vol: int, leverage: int,
            price: str,
            **params
    ):
        url = "https://futures.mexc.com/api/v1/private/order/create"
        data = {
            "symbol": symbol,
            "side": info[side],
            "openType": info[openType],
            "type": info[type],
            "vol": vol,
            "leverage": leverage,
            "price": price,
            **params
        }

        data, sign, ts = get_data(self.fingerprint, data, self.token)

        self.userAgent['x-mxc-sign'] = sign
        self.userAgent['x-mxc-nonce'] = ts
        self.userAgent['Authorization'] = self.token

        headers = self.userAgent
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=data) as response:
                return await response.json()

    async def changeOrderSLTP(
            self, orderId: str, stopLossPrice: str, takeProfitPrice: str
    ):
        url = "https://futures.mexc.com/api/v1/private/stoporder/change_price"
        data = {
            "orderId": orderId,
            "stopLossPrice": stopLossPrice,
            "takeProfitPrice": takeProfitPrice,
        }

        data, sign, ts = get_data(self.fingerprint, data, self.token)

        self.userAgent['x-mxc-sign'] = sign
        self.userAgent['x-mxc-nonce'] = ts
        self.userAgent['Authorization'] = self.token

        headers = self.userAgent
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=data) as response:
                return await response.json()

    async def closeAll(
            self
    ):
        url = "https://futures.mexc.com/api/v1/private/position/close_all"
        data = {}

        data, sign, ts = get_data(self.fingerprint, data, self.token)

        self.userAgent['x-mxc-sign'] = sign
        self.userAgent['x-mxc-nonce'] = ts
        self.userAgent['Authorization'] = self.token

        headers = self.userAgent
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=data) as response:
                return await response.json()

    async def cancelAll(
            self
    ):
        url = "https://futures.mexc.com/api/v1/private/position/cancel_all"
        data = {}

        data, sign, ts = get_data(self.fingerprint, data, self.token)

        self.userAgent['x-mxc-sign'] = sign
        self.userAgent['x-mxc-nonce'] = ts
        self.userAgent['Authorization'] = self.token

        headers = self.userAgent
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=data) as response:
                return await response.json()

    async def openPositions(
            self
    ):
        url = "https://futures.mexc.com/api/v1/private/position/open_positions"

        data = {}
        data, sign, ts = get_data(self.fingerprint, data, self.token)
        self.userAgent['x-mxc-sign'] = sign
        self.userAgent['x-mxc-nonce'] = ts
        self.userAgent['Authorization'] = self.token

        headers = self.userAgent
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, json=data) as response:
                return await response.json()

    async def openOrders(
            self
    ):
        url = "https://futures.mexc.com/api/v1/private/order/list/open_orders"

        data = {}
        data, sign, ts = get_data(self.fingerprint, data, self.token)

        self.userAgent['x-mxc-sign'] = sign
        self.userAgent['x-mxc-nonce'] = ts
        self.userAgent['Authorization'] = self.token

        headers = self.userAgent
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, json=data) as response:
                return await response.json()
