import requests
from pprint import pprint

url_api = requests.get("https://api.github.com/users/romodulo")
keysShortcut = list(url_api.json().keys())
stored = dict(url_api.json())
pprint(stored)

