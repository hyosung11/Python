import config
import tweepy
import time
# from twython import Twython, TwythonError

# create a Twython object by passing the necessary secret passwords
# twitter = Twython(config.api_key, config.api_secret,
#                   config.access_token, config.token_secret)

auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
auth.set_access_token(config.access_token, config.token_secret)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

user = api.me()

# print(user.name)
# print(user.screen_name)
# print(user.followers_count)


# ===============================

# Follower Bot

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)

# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.name == '류진우':
#         follower.follow()
#         break


# like a tweet

search_string = 'smart contracts'
numberOfTweets = 3

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as error:
        print(error.reason)
    except StopIteration:
        break


