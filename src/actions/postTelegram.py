from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)

import sys
import requests
import os
import json

def get_credentials(app_name):
    credentials_file  = '../' + os.getenv('CREDENTIALS_FILE')
    f_config = open(credentials_file, 'r')
    try :
        credentials = json.load(f_config)[app_name]
    except KeyError:
        print('There is no credentials for this app name')
        exit()
    f_config.close()
    return credentials

def main ():
    if (len(sys.argv) != 2):
        print ("argumentos mal")
        exit()

    telegram_chat_id = sys.argv[1]

    file_name = '../' + os.getenv('TWITTER_TELEGRAM_BUFFER_FILE')

    credentials = get_credentials('telegram')

    bot_token = os.getenv ('TELEGRAM_BOT_TOKEN')
    
    try:
        chat_id = credentials[telegram_chat_id]['chat_id']
    except KeyError:
        print('There is no credentials for this telegram group')
        exit()

    messages = json.load(open(file_name, "r")) 

    try:
        tuit = messages[telegram_chat_id][0]
    except IndexError:
        print("There is no data for this telegram group")
        exit()
    
    if tuit['text'].startswith('RT @'):
        tuit['text'] = tuit['text'].replace('RT @', '🔁 RT https://twitter.com/', 1)

    text = tuit['text'] + '\n\n' + 'Enlace:' + tuit['url'] + '\n\n' +'🐦 Este es el nuevo tuit de https://twitter.com/' + tuit['user']

    
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' +  chat_id + '&parse_mode=Markdown&text=' + text

    try:
        response = requests.get(send_text)
    except requests.exceptions.RequestException as e:
        print(e)
        exit()

    del messages[telegram_chat_id][0]

    json.dump(messages, open(file_name, "w"))

if __name__ == "__main__":
    main()
