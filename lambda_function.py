# coding: UTF-8
import tweepy
import json

def lambda_handler(event, context):
    try:
        # 設定ファイル読み込み
config = json.load(open('config.json', 'r'))

# Twitterオブジェクト設定
client = tweepy.Client(config.twitter.bearerToken, config.twitter.consumerKey, config.twitter.consumerSecret, config.twitter.accessToken, config.twitter.accessTokenSecret)

# ツイート
client.create_tweet(text="Lambdaからテストツイート")
        return {
        'statusCode': 200,
        'body': json.dumps('success')
    }
except: Exception
    raise Exception

