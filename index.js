const http = require('http');
const Config = require('./config.js').Config;
const MY_WEATHER_APIKEY = Config.openWeatherMap.apiKey;
const LAT = 33.60639; //緯度
const LON = 130.41806; //経度
const req = 'http://api.openweathermap.org/data/2.5/weather?lat=' + LAT + '&lon=' + LON + '&appid=' + MY_WEATHER_APIKEY + '&lang=ja';
const Twitter = require('twitter');
const client = new Twitter({
  consumer_key: Config.twitter.apiKey,
  consumer_secret: Config.twitter.secretKey,
  access_token_key: Config.twitter.accessToken,
  access_token_secret: Config.twitter.secretToken,
  bearer_token: Config.twitter.bearerToken
});

exports.handler = function(event, context) {
  tweetPost("Lambdaからテストツイート");
  http.get(req, function(res) {
    console.log("Got response: " + res.statusCode);
    res.setEncoding('utf8');
    res.on("data", function(chunk) {
      context.done(null, JSON.parse(chunk));
    });
  }).on('error', function(e) {
    context.done('error', e);
  });
};

function tweetPost(content) {
  console.log("ツイート開始");
  client.post('statuses/update', { status: content }, function(error, tweet, response) {
    if (!error) {
      console.log("tweet success: " + content);
    }
    else {
      console.log(error);
    }
  });
}
