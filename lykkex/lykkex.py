import requests


class LykkexConstants(object):
    ORDER_BOOKS_RELATIVE_URL = "OrderBooks"
    BASE_URL = "https://hft-service-dev.lykkex.net/api/"
    IS_ALIVE_RELATIVE_URL = "IsAlive"


def is_alive():
    return requests.get(LykkexConstants.BASE_URL + LykkexConstants.IS_ALIVE_RELATIVE_URL).json()


def get_order_books():
    return requests.get(LykkexConstants.BASE_URL + LykkexConstants.ORDER_BOOKS_RELATIVE_URL).json()


def get_order_book(asset_pair_id):
    return requests.get(
        LykkexConstants.BASE_URL + LykkexConstants.ORDER_BOOKS_RELATIVE_URL + '/' + asset_pair_id).json()
