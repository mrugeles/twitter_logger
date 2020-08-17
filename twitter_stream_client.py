import sys
import json
import tweepy
import logging
logging.basicConfig(filename='/var/log/twitter/tweets_logs.log', level=logging.INFO, format='%(message)s')


class TwitterStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        logging.info(status._json)


def read_tweets(access_keys):
    auth = tweepy.OAuthHandler(access_keys['consumer_key'], access_keys['consumer_secret'])
    auth.set_access_token(access_keys['access_token'], access_keys['access_token_secret'])

    api = tweepy.API(auth)

    stream_listener = TwitterStreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
    stream.sample()


if __name__ == "__main__":

    if len(sys.argv) == 2:
        with open(sys.argv[1]) as json_file:
            config = json.load(json_file)
            read_tweets(config)
