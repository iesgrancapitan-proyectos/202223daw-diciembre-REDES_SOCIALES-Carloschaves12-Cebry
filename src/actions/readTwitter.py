from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)

import sys
import requests
import os
import json
import tweepy
import datetime


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

def update_credentials(id_cuenta, fecha):
    new_credentials = json.load(open('../' + os.getenv('CREDENTIALS_FILE'), 'r'))
    new_credentials['twitter'][id_cuenta]['last_time_read'] = fecha
    json.dump (new_credentials, open('../' + os.getenv('CREDENTIALS_FILE'), 'w'))

def getTweets(credentials,id_cuenta):
    new_items = {}
    bearer_token = credentials[id_cuenta]['bearer_token']
    user_name = credentials[id_cuenta]['user_name']
    try:
        client = tweepy.Client(bearer_token=bearer_token)
        user = client.get_user(username=user_name)
        fecha = credentials[id_cuenta]['last_time_read']

        # fecha = la fecha de hace 1 semana
        fecha = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%SZ")
        response = client.get_users_tweets(id=user.data.id, start_time=fecha)
        
        fecha = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        update_credentials(id_cuenta, fecha)

    except tweepy.errors.Forbidden as e:
        print(e)

    if response.data:
        print(response)
        for tweet in response.data:
            new_items[tweet.id] = {
                'id' : tweet.id,
                'text' : tweet.text,
                'url' : 'https://twitter.com/' + user_name + '/status/' + tweet.id.__str__(),
                'user' : user_name,
            }
    return new_items

def main ():
    if len(sys.argv) != 1:
        print('nombreSript.py')
        exit()

    file_name = '../' + os.getenv('TWITTER_TELEGRAM_BUFFER_FILE')
    content = get_json(file_name)
    credentials = get_credentials('twitter')

    for id_cuenta in credentials:
        new_items = getTweets(credentials,id_cuenta)
        content = add_items(content, new_items, id_cuenta)
    
    json.dump(content, open(file_name, 'w'))

if __name__ == '__main__':
    main()