import requests


def build_url(base, params):
    r = requests.Request("GET", base, params=params)
    url = r.prepare().url
    return url

