try:
    from urllib.request import Request, urlopen  # Python 3
except:
    from urllib2 import Request, urlopen  # Python 2
import json

class LykkexConstants(object):
    ORDER_BOOKS_RELATIVE_URL = "OrderBooks"
    BASE_URL = "https://hft-service-dev.lykkex.net/api/"
    IS_ALIVE_RELATIVE_URL = "IsAlive"
    WALLET_URL = 'https://hft-service-dev.lykkex.net/api/Wallets'
    BASE_HEADERS = {'api-key': api_key, 'Content-Type': 'application/json'}

def is_alive():
    return json.loads(urlopen(LykkexConstants.BASE_URL + LykkexConstants.IS_ALIVE_RELATIVE_URL).read().decode())

def get_order_books():
    return json.loads(urlopen(LykkexConstants.BASE_URL + LykkexConstants.ORDER_BOOKS_RELATIVE_URL).read().decode())

def get_order_book(asset_pair_id):
    return json.loads(urlopen(LykkexConstants.BASE_URL + LykkexConstants.ORDER_BOOKS_RELATIVE_URL + '/' + asset_pair_id).read().decode())

def get_balance(api_key):
    return json.loads(urlopen(Request(LykkexConstants.WALLET_URL, headers = LykkexConstants.BASE_HEADERS)).read().decode())
    
def get_pending_orders(api_key):
    return json.loads(urlopen(Request(LykkexConstants.BASE_URL + 'Orders?status=InOrderBook', headers = LykkexConstants.BASE_HEADERS)).read().decode())
  
def send_market_order(api_key, asset_pair, asset, order_action='BUY', volume='0.1'):
    data = json.dumps(
        {"AssetPairId": asset_pair, "Asset": asset, "OrderAction": order_action,
         "Volume": volume}).encode("utf8")
    return json.loads(urlopen(Request(LykkexConstants.BASE_URL + 'Orders/market', data, LykkexConstants.BASE_HEADERS)).read())
  
def send_limit_order(api_key, asset_pair, asset, price, order_action='BUY', volume='0.1'):
     data = json.dumps(
        {"AssetPairId": asset_pair, "Asset": asset, "OrderAction": order_action,
         "Volume": volume, "Price": price}).encode("utf8")
     return json.loads(urlopen(Request(LykkexConstants.BASE_URL + 'Orders/limit', data, LykkexConstants.BASE_HEADERS)).read())

def control_limit_order(api_key, order_id):
     return json.loads(urlopen(Request(LykkexConstants.BASE_URL + 'Orders/'+order_id, headers=LykkexConstants.BASE_HEADERS)).read())
  