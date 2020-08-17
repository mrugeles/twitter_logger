import sys
import json
import tweepy
import logging
logging.basicConfig(filename='logs/tweets_logs.log', level=logging.INFO)


class TwitterStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        logging.info(status)


def read_tweets(access_keys):
    auth = tweepy.OAuthHandler(access_keys['consumer_key'], access_keys['consumer_secret'])
    auth.set_access_token(access_keys['access_token'], access_keys['access_token_secret'])

    api = tweepy.API(auth)

    stream_istener = TwitterStreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=stream_istener)
    stream.sample()


if __name__ == "__main__":

    if len(sys.argv) == 2:
        with open(sys.argv[1]) as json_file:
            config = json.load(json_file)
            read_tweets(config)
