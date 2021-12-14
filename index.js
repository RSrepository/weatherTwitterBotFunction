const http = require('http');
const Config = require('./config.js').Config;

exports.handler = function(event, context) {
    const http = require('http');
    const MY_WEATHER_APIKEY = Config.openWeatherMap.apiKey;
    const LAT = 33.60639; //緯度
    const LON = 130.41806; //経度
    const req = 'http://api.openweathermap.org/data/2.5/weather?lat=' + LAT + '&lon=' + LON + '&appid=' + MY_WEATHER_APIKEY + '&lang=ja';

    console.log('value1 = ' + event.key1);
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
