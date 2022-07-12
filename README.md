# DiscordTwitch-WebbookNotifier

I made this to help small streamers or devoted fans to tell if they/them are live through discord webhook(bypasses created a bot).
Checks if streamer is live ever x amout of seconds(i rec 2 mins(120 seconds)

## Description

Pretty Hard to setup but please just read the code and follow directions!

## Getting Started

### Dependencies

1. https://github.com/lovvskillz/python-discord-webhook libary for sending webhooks
2. https://dev.twitch.tv/ for seeing streamer data

### Installing
PLEASE HAVE SOME PYTHON KNOWLEDGE
First install lovveskillz python libary link in dependencies.
Then you want to set up a twitch application(i wont walk you through this plenty of tutorials on youtube)
Once you have your application approved youll need 2 things your client secret and client id
you can only copy your client secret once so be carful!
now that you have boths those keys we can get to the code.
you're gonna need python 3.10 or above.
Youll need a python ide i reccomend pycharm(https://www.jetbrains.com/pycharm/)
open the project
goto "def genToken()"
this is where youll paste your client id and client secret
also you need to paste your client id one more other place and thats at the bottom in the main method
example here:
![alt text](https://i.imgur.com/8ZrSSsZ.png)
Now you need to setup a discord webhook in a channel please watch a video on youtube on how to make one its like 4 buttons
once you have a discord webhook set up copy the url
then goto
![alt text](https://i.imgur.com/isoGHea.png)
paste your webhook in there where it says 'WEBHOOK-URL'
and thats it!
save and run the script!
## Screenshot of it working
![alt text](https://i.imgur.com/JXe2QBS.png)
