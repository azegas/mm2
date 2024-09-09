# mm2 

Magic mirror 2

# TODO

- [x] alphavantage - tik 25 queires KRC - https://www.alphavantage.co/documentation/
- [ ] stocks - most advanced most declined
- [ ] stocks - top gainers
- [ ] stocks - top losers
- [x] stocks - volume
- [ ] quote of the day
- [ ] google trends topics - https://trends.google.com/trending?geo=US
- [ ] notification when big change happened or smth like that. or simply show todays trends in telegram kaip zinute
- [ ] raspberry pi uptime 
- [x] Running eilutė kaip NASDAQe (labai trukineja ji raspberryje)
- [ ] fondu duomenys - https://www.swedbank.lt/private/investor/funds/allFunds/list/details
- [x] humidity inside
- [x] temperature in
- [x] temperature out
- [ ] humidity UI sitaip SEK TIK 24h - https://i0.wp.com/blog.balena.io/wp-content/uploads/2021/07/sensev2.png?fit=1200%2C628&ssl=1
- [x] log file for when was fetched and if successs or not (aisku matai in flask terminal, but anyway)
- [ ] switch one the display kai kas nors priarteja - https://tutorials-raspberrypi.com/connect-and-control-raspberry-pi-motion-detector-pir/, https://www.youtube.com/watch?v=Tw0mG4YtsZk
- [X] fix period for charts!!! make it dynamic
- [x] covid cases (not so needed and kinda hard to fetch)
- [x] population (not so needed and kinda hard to fetch)
- [x] indication, that the page has refreshed


# Docs

## packages

`source ~/venvs/venv-mm2/bin/activate`

```sh
# web app
pip install flask flask-socketio python-dotenv beautifulsoup4 requests
# humidity sensor
pip install adafruit-circuitpython-dht
```

## ssh

Connect to pi from windows:
```pwsh
ssh arvypi@raspberrypi.local
# or:
ssh arvypi@192.168.0.82
```

TTransfer files from local directory to raspberry - `tranfer.bat`

## crontab

# crontab -l > cron.txt
# crontab cron.txt
# crontab -e
# crontab -l


## How it works with socket.io

Backend:
- continuous process on the backend to fetch the data (cronjob)
- cronjob fetches every minute or so during 05:00 - 07:00 and 17:00 - 22:00
- when the cron job finished, usually it stores the results in a .json file

Frontend:
- on the frontend, we have a flask app
- flask app in itself has some socketio functions that READ data from the files
- We tell, with the help of javascript, how often to read the data of those files and then update the page with it


## Humidity sensor

# humidity_pi

```sh
arvypi@raspberrypi:~ $ cat /proc/cpuinfo | grep Model
Model           : Raspberry Pi 3 Model B Rev 1.2
```

Pin info - https://i.pinimg.com/736x/bf/e5/02/bfe502b80a3248ed48fb125182235c32.jpg

-----------------

## Humidity sensor

I have humidity sensor and I want to read the humidity from it and print it to the console.

I want to do this every second. my sensor is DHT22 - https://www.anodas.lt/dht22-temperaturos-ir-dregmes-jutiklis-su-pcb

```
Temperature: 25.5°C, Humidity: 67.2%
Temperature: 25.5°C, Humidity: 67.1%
Temperature: 25.5°C, Humidity: 67.1%
Temperature: 25.5°C, Humidity: 67.2%
Temperature: 25.5°C, Humidity: 67.2%
Temperature: 25.5°C, Humidity: 66.9%
Temperature: 25.5°C, Humidity: 66.9%
Temperature: 25.5°C, Humidity: 67.6%
Temperature: 25.5°C, Humidity: 67.6%
```

## motion sensor

I have such motion sensor - https://www.anodas.lt/hc-sr501-pir-judesio-daviklis?search=PIR

its pins - https://images.theengineeringprojects.com/image/main/2019/01/Introduction-to-HC-SR501.jpg

- TODO try to control delay
- TODO try to control sensitivity