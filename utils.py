import requests


def fetch_page(url):
    """ fetch page of url in attr and return it"""
    return requests.get(url)
