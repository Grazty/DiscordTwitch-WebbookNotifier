import time

from discord_webhook import DiscordWebhook
import requests
from datetime import datetime, timedelta
from discord_webhook import DiscordWebhook, DiscordEmbed
import json



def genToken():
    client_id = 'client-id'
    client_secret = 'client-secret'

    body = {
        'client_id': client_id,
        'client_secret': client_secret,
        "grant_type": 'client_credentials'
    }
    r = requests.post('https://id.twitch.tv/oauth2/token', body)
    keys = r.json();
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

def getList(dict):
    return dict.keys()

def isstreamerlive(client_id, keys, streamer):
    hassent = 0
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
            if hassent == 1:
                print("stream is still live")
            else:
                sendwebHook(stream_data2[0]['user_name'], 'https://www.twitch.tv/' + stream_data2[0]['user_name'], stream_data2[0]['game_name'], 'https://static-cdn.jtvnw.net/previews-ttv/live_user_' + stream_data2[0]['user_login'] + '-800x800.jpg', stream_data2[0]['title'])
                print('live')
                hassent = 1
        else:
            print('not live')
            break;
            hassent = 0
        time.sleep(120)


def sendwebHook(streamer, streamerurl, game, thumbnailurl, title):
    webhook = DiscordWebhook(url='WEBHOOK-URL')

    # create embed object for webhook
    embed = DiscordEmbed(title=title,  color='03b2f8')

    # set author
    embed.set_author(name=streamer + ' is live!', url=streamerurl)

    # set image
    embed.set_image(url=thumbnailurl)



    # add fields to embed
    embed.add_embed_field(name='Game', value=game)

    # add embed object to webhook
    webhook.add_embed(embed)

    response = webhook.execute()

if __name__ == '__main__':
    f2 = open("expire.txt", "r")
    datestr = f2.read()
    if datestr == '':
        genToken()
    f2.close()
    datetime2 = datetime.strptime(datestr, '%Y-%m-%d')
    datetime1 = datetime.today()
    f2.close()
    if datetime2 < datetime1:
        print('Token has expired generating a new one!')
        genToken()
    else:
        print('Token has not expired')

    f = open("appToken.txt", "r")
    contents = f.read()
    f.close()
    if contents != '':
        isstreamerlive('CLIENT-ID', contents, 'streamername')
    else:
        genToken()

