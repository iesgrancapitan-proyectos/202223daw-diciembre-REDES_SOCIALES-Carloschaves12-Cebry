import json
import sys
import tweepy
from dotenv import load_dotenv
from pathlib import Path
import os

dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)

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

def get_client( user_id):
    credentials = get_credentials('twitter')

    try :
        return tweepy.Client(consumer_key=credentials[user_id]['consumer_key'],
        consumer_secret=credentials[user_id]['consumer_secret'],
        access_token=credentials[user_id]['access_token'],
        access_token_secret=credentials[user_id]['access_token_secret'])
    except KeyError:
        print('There is no credentials for this twitter account')
        exit()

def create_text(data, user_id):
    try:
        return data[0]['given_title'] + "\n" + data[0]['given_url']
    except KeyError:
        print("There is no credentials for this twitter account")
        exit()
    except IndexError:
        print("There is no tweets for this twitter account")
        exit()

def main():
    if (len(sys.argv) != 2):
        print ("argumentos mal")
        exit()

    file_name = '../' + os.getenv('POCKET_TWITTER_BUFFER_FILE')

    user_id = sys.argv[1]

    client = get_client(user_id)

    all_data = json.loads(open(file_name, "r").read())

    data = all_data[user_id]

    tweet = create_text(data, user_id)

    try:
        response = client.create_tweet(text=tweet)
    except tweepy.errors.Forbidden as e:
        print(e)
    finally:
        del data[0]
        json.dump(all_data, open(file_name, "w"))

if __name__ == "__main__":
    main()