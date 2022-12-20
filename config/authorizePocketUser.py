import requests
import webbrowser
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)

# https://getpocket.com/developer/docs/authentication
# 1º Necesitamos obtener una platform consumer key
# http://getpocket.com/developer/apps/new
consumer_key = os.getenv('POCKET_CONSUMER_KEY')
 
# 2º Necesitamos obtener un request token
url_request_token = 'https://getpocket.com/v3/oauth/request'
redirect_uri = os.getenv('REDIRECT_URI')
d = {'consumer_key': consumer_key,'redirect_uri' : redirect_uri}
h = {'X-Accept': 'application/json'}

request_1 = requests.post(url_request_token,json=d,headers=h)

if request_1.status_code != 200:
    print(request_1.headers['X-Error-Code'], request_1.headers['X-Error'])
    exit()
    
print ()
request_token = request_1.json()['code']

# 3º Redirect user to Pocket to continue authorization
# https://getpocket.com/auth/authorize?request_token=YOUR_REQUEST_TOKEN&redirect_uri=YOUR_REDIRECT_URI
template_url_continue_authorizacion = 'https://getpocket.com/auth/authorize?request_token=YOUR_REQUEST_TOKEN&redirect_uri=YOUR_REDIRECT_URI'
url_continue_authorizacion = template_url_continue_authorizacion.replace('YOUR_REQUEST_TOKEN',request_token).replace('YOUR_REDIRECT_URI', redirect_uri)
print (url_continue_authorizacion)

# 4º Receive the callback from Pocket
# webbrowser.open(url_continue_authorizacion)
input('press Enter when authorized...\n')

# 5º Convert a request token into a Pocket access token
d_2 = {'consumer_key': consumer_key,'code' : request_token}
url_request_authorize ='https://getpocket.com/v3/oauth/authorize'
request_2 = requests.post(url_request_authorize,json=d_2,headers=h)


if request_2.status_code != 200:
    print(request_2.headers['X-Error-Code'], request_2.headers['X-Error'])
    exit()

username=request_2.json()['username']
access_token=request_2.json()['access_token']

print(username, access_token)