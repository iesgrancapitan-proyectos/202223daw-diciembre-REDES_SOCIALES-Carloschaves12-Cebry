from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)

import sys
import requests
import os
import json

CONSUMER_KEY = os.getenv('POCKET_CONSUMER_KEY')

def get_credentials(app_name):
    credentials_file  = '../' + os.getenv('CREDENTIALS_FILE')
    f_config = open(credentials_file, 'r')
    try :
        credentials = json.load(f_config)[app_name]
    except KeyError:
        print('No hay credenciales de pocket')
        exit()
    f_config.close()
    return credentials

def get_pocket_items (access_token, tag):
    URL_REQUEST = 'https://getpocket.com/v3/get'
    d = {
        'consumer_key': CONSUMER_KEY,'access_token' : access_token,
        'tag' : tag,
        'detailType' : 'complete'
        }
    request = requests.post(URL_REQUEST,json=d)
    if request.status_code != 200:
        print(request.headers['X-Error-Code'], request.headers['X-Error'])
        exit()

    return request.json()['list']

def get_json(file_name):

    if os.path.exists(file_name) != True:
        file = open(file_name, 'w')
        file.write(json.dumps({}))
        file.close()

    file = open(file_name, 'r') 
    file_content = json.load(file)
    file.close()
    
    return file_content

def add_items (content, new_items, tag):
    if content.get(tag) == None:
        content[tag] = []

    for key in new_items:
        item = new_items[key]
        content[tag].append(item)

    return content

def rewrite_json(file_name, content):
    f_output = open(file_name, 'w')
    f_output.write(json.dumps(content))
    f_output.close()

def delete_items (access_token, items):
    URL_REQUEST = 'https://getpocket.com/v3/send'
    actions = []

    for key in items:
        actions.append({'action': 'delete', 'item_id': key})

    d = {
        'consumer_key': CONSUMER_KEY,
        'access_token' : access_token,
        'actions' : actions
        }
    
    request = requests.post(URL_REQUEST,json=d)
    
    if request.status_code != 200:
        print(request.headers['X-Error-Code'], request.headers['X-Error'])
        exit()

def main ():
    if len(sys.argv) != 1:
        print('nombreSript.py')
        exit()
    
    pocket_twitter_buffer_name = '../' + os.getenv('POCKET_TWITTER_BUFFER_FILE')
    pocket_twitter_buffer_content = get_json(pocket_twitter_buffer_name)
        
    pocket_credentials = get_credentials('pocket')
    new_items = {}

    for pocket_user_id in pocket_credentials:
        pocket_user_data = pocket_credentials[pocket_user_id]
        access_token = pocket_user_data['access_token']
        for tag in pocket_user_data['tags']:
            new_items[tag] = get_pocket_items(access_token, tag)
            pocket_twitter_buffer_content = add_items(pocket_twitter_buffer_content, new_items[tag], tag)
            if len(new_items[tag]) != 0:
                delete_items(access_token, new_items[tag])
    rewrite_json(pocket_twitter_buffer_name, pocket_twitter_buffer_content)

if __name__ == '__main__':
    main()
