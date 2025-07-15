import tweepy
from transformers import pipeline
api_key="puzgCMUJ4NPj3SUXgbLxVVCkW"
api_key_secret="91t1ZsybERiAAeo7Jl5cJHFLBFW6QFLFkjEUGJlyI1iJQz1EX4"
access_token="1944994626089443329-TgzB7qje5mly36MYeM1q0zYKxGITL3"
access_token_secret="sIeGonFTRwiqY0Kwo3t1IivM3ZpUHw3uYkQ7EG7uDnZ14"
auth=tweepy.OAuth1UserHandler(api_key,api_key_secret,access_token,access_token_secret)
api=tweepy.API(auth)
sentimental_analyzer=pipeline("sentiment-analysis")
api.search_tweets(q="#INDvsENG",lang="en",count=10)