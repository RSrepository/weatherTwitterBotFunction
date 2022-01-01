import sys
sys.path.append('python_package')
# coding: UTF-8
import json
import tweepy
import random
import requests

def lambda_handler(event, context):
    # 設定ファイル読み込み
    config = json.load(open('config.json', 'r'))
    # Twitterオブジェクト設定
    client = tweepy.Client(config['twitter']['bearerToken'], config['twitter']['consumerKey'],
                           config['twitter']['consumerSecret'], config['twitter']['accessToken'], config['twitter']['accessTokenSecret'])
    # 今日の天気情報を取得(東京都,名古屋市,大阪市からランダムで)
    weather = get_today_weather(config['openWeatherMap']['apiKey'])
    # アイコン画像URLを設定
    icon_url = 'http://openweathermap.org/img/w/' + weather['weather'][0]['icon'] + '.png';
    # ツイート
    client.create_tweet(text=weather['name'] + weather['weather'][0]['main'],filename=icon_url)

# 天気情報を取得するメソッド
def get_today_weather(api_key):
    # 東京都,名古屋市,大阪市からランダム
    city_list = ['東京都','名古屋市','大阪市']
    random.shuffle(city_list)
    # APIのURL設定
    api = 'http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&appid={key}&lang=ja'
    url = api.format(city = city_list[0], key = api_key)
    # レスポンスをjsonで返す
    return requests.get(url).json()
