import time

from discord_webhook import DiscordWebhook
import requests
from datetime import datetime, timedelta
from discord_webhook import DiscordWebhook, DiscordEmbed
import json


class Contents:
    def __init__(self, clientid = '', clientSecret = '', streamername = '', hassent = 0, datestr = '', webhookURL = '', timeinsec = 0):
        self._clientid = clientid
        self._clientSecret = clientSecret
        self._streamername = streamername
        self._hassent = hassent
        self._datestr = datestr
        self._webhookURL = webhookURL
        self._timeinsec = timeinsec

    def get_clientid(self):
        return self._clientid

    def set_clientid(self, x):
        self._clientid = x

    def get_clientSecret(self):
        return self._clientSecret

    def set_clientSecret(self, x):
        self._clientSecret = x

    def get_streamername(self):
        return self._streamername

    def set_streamername(self, x):
        self._streamername = x

    def get_hassent(self):
        return self._hassent

    def set_hassent(self, x):
        self._hassent = x

    def get_datestr(self):
        return self._datestr

    def set_datestr(self, x):
        self._datestr = x

    def get_webhookURL(self):
        return self._webhookURL

    def set_webhookURL(self, x):
        self._webhookURL = x

    def get_timeinsec(self):
        return self._timeinsec

    def set_timeinsec(self, x):
        self._timeinsec = x

def genToken():
    body = {
        'client_id': setget.get_clientid(),
        'client_secret': setget.get_clientSecret(),
        "grant_type": 'client_credentials'
    }
    r = requests.post('https://id.twitch.tv/oauth2/token', body)
    keys = r.json()
    f2 = open("expire.txt", "w")
    f = open("appToken.txt", "w")
    f.write(keys['access_token'])
    current_date = datetime.now()
    end_date = current_date + timedelta(days=60)  # Adding 60 days.
    end_date_formatted = end_date.strftime('%Y-%m-%d')
    f2.write(end_date_formatted)
    f.close()
    f2.close()
    print(keys)
    print('Generated a Application token!')


def isstreamerlive(client_id, keys, streamer):
    headers = {
        'Client-ID': client_id,
        'Authorization': 'Bearer ' + keys
    }
    print(headers)
    while True:
        stream = requests.get('https://api.twitch.tv/helix/streams?user_login=' + streamer, headers=headers)
        stream_data = stream.json()
        print(stream_data)
        stream_data2 = stream_data['data']
        if len(stream_data['data']) == 1:
            if setget.get_hassent() == 1:
                print("stream is still live")
            else:
                sendwebHook(stream_data2[0]['user_name'], 'https://www.twitch.tv/' + stream_data2[0]['user_name'], stream_data2[0]['game_name'], 'https://static-cdn.jtvnw.net/previews-ttv/live_user_' + stream_data2[0]['user_login'] + '-800x800.jpg', stream_data2[0]['title'])
                print('live')
                setget.set_hassent(1)
        else:
            print('not live')
            break;
            setget.set_hassent(0)
        time.sleep(int(setget.get_timeinsec()))


def sendwebHook(streamer, streamerurl, game, thumbnailurl, title):
    webhook = DiscordWebhook(url=setget.get_webhookURL())
    embed = DiscordEmbed(title=title,  color='03b2f8')
    embed.set_author(name=streamer + ' is live!', url=streamerurl)
    embed.set_image(url=thumbnailurl)
    embed.add_embed_field(name='Game', value=game)
    webhook.add_embed(embed)
    response = webhook.execute()


if __name__ == '__main__':
    setget = Contents()

    print('Please enter Client-ID: ')
    setget.set_clientid(input())

    print('Please Enter Client-Secret: ')
    setget.set_clientSecret(input())

    print('Please Enter Streamers Username: ')
    setget.set_streamername(input())

    print('Please Enter Discord Webhook-URL: ')
    setget.set_webhookURL(input())

    print('Please Enter How many seconds you want to check status of streamer(rec: 120) : ')
    setget.set_timeinsec(input())

    f2 = open("expire.txt", "r")
    datestr = f2.read()
    if datestr == '':
        genToken()
    datestr = f2.read()
    f2.close()
    datetime2 = datetime.strptime(datestr, '%Y-%m-%d')
    datetime1 = datetime.today()
    if datetime2 < datetime1:
        print('Token has expired generating a new one!')
        genToken()
    else:
        print('Token has not expired')

    f = open("appToken.txt", "r")
    contents = f.read()
    f.close()
    if contents != '':
        isstreamerlive(setget.get_clientid(), contents, setget.get_streamername())
    else:
        genToken()

