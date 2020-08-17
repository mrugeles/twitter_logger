import sys
import json
import tweepy
import logging

from json import JSONEncoder

logging.basicConfig(filename='/var/log/twitter/tweets_logs.log', level=logging.INFO, format='%(message)s')


class StatusEncoder(JSONEncoder):
    def default(self, o):
        if hasattr(o, '__dict__'):
            o.__dict__.pop('_api', None)
            o.__dict__.pop('_json', None)
            return o.__dict__
        return str(o)


class TwitterStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        logging.info(StatusEncoder().encode(status))


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
