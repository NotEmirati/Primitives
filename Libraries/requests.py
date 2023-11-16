import requests

def get_url(s: str):
    return requests.get(s)

url = 'https://api.github.com'
print(get_url(url))
