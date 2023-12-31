import requests

def get_url(s: str):
    return requests.get(s)

url = 'https://api.github.com'
print(get_url(url))

response = requests.get('https://api.github.com')
print(response.status_code)

def check_connection(s: str):
    response = requests.get(s)
    if response.status_code == 200:
        print('Success!')
    elif response.status_code == 404:
        print('Not Found.')

print(response.url)


import requests
from requests.auth import HTTPBasicAuth

response = requests.get('https://api.github.com / user, ',
                        auth=HTTPBasicAuth('user', 'pass'))
print(response)

# import requests module 
import requests 
  
# create a session object 
s = requests.Session() 
  
# make a get request 
s.get('https://httpbin.org/cookies/set/sessioncookie/123456789') 
  
# again make a get request 
r = s.get('https://httpbin.org/cookies') 
  
# check if cookie is still set 
print(r.text) 
