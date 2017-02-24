import twitter
from secret_env import *
def connect():
    api = twitter.Api(consumer_key=MY_CONSUMER_KEY,
                          consumer_secret=MY_CONSUMER_SECRET,
                          access_token_key=MY_ACCESS_TOKEN_KEY,
                          access_token_secret=MY_ACCESS_TOKEN_SECRET)
    return api

TWEET_HISTORY = "tweet_history.log"
LAMBCHOPS_SONG = [
    "It's the tweet storm that doesn't end",
    "Yes, it goes on and on my friend",
    "Somebody started tweeting it not knowing what it was",
    "And they'll just keep retweeting it forever just because"
]

if __name__=="__main__":

    api = connect()

    history = open(TWEET_HISTORY).read().split("|")
    last_status = int(history[0])
    history_length = int(history[1])
    
    line_id = (history_length - 1 ) % 4

    status = api.PostUpdate("%s... (%d/?)" % (LAMBCHOPS_SONG[line_id], (history_length + 1)), in_reply_to_status_id=last_status)

    status_id = status.id

    line = "%d|%d" % (status_id, history_length + 1 )

    with open(TWEET_HISTORY, "w") as f:
        f.write(line)
        f.close()

