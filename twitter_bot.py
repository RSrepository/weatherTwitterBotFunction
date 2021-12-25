# coding: UTF-8
import tweepy
import json

# 設定ファイル読み込み
config = json.load(open('config.json', 'r'))

# Twitterオブジェクト設定
client = tweepy.Client(config.twitter.bearerToken, config.twitter.consumerKey, config.twitter.consumerSecret, config.twitter.accessToken, config.twitter.accessTokenSecret)

# ツイート
client.create_tweet(text="Lambdaからテストツイート")