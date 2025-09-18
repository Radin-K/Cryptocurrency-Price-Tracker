from Constant import constant_api
import requests
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
header = {
    "Accept": "application/json",
    'X-CMC_PRO_API_KEY': constant_api
}
params = {
    "start": 1,
    "limit": 10,
    'convert': "USD"
}
res = requests.get(url, headers=header, params=params)
res.raise_for_status()
data = res.json()
for coin in data['data']:
    symbol = coin['symbol']
    price = coin['quote']['USD']['price']
    change_1h = coin['quote']['USD']['percent_change_1h']
    print(symbol, price, change_1h)

