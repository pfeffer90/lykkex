import requests


class LykkexConstants(object):
    BASE_URL = "https://hft-service-dev.lykkex.net/api/"


def is_alive():
    return requests.get(LykkexConstants.BASE_URL + "IsAlive").json()
