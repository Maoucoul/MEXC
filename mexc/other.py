from sign import get_data
import aiohttp


async def userInfo(
        token: str, fingerprint, userAgent
):
    url = "https://www.mexc.com/ucenter/api/user_info"
    data = {}

    data, sign, ts = get_data(fingerprint, data, token)

    headers = {userAgent.format(sign, ts, token)}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, json=data) as response:
            return await response.json()
