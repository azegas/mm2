# invest

- [x] alphavantage - tik 25 queires KRC - https://www.alphavantage.co/documentation/
- [ ] most advanced most declined
- [ ] top gainers
- [ ] top losers
- [x] volume
- [ ] google trends topics - https://trends.google.com/trending?geo=US
- [ ] notification when big change happened or smth like that. or simply show todays trends in telegram kaip zinute
- [x] Running eilutė kaip NASDAQe (labai trukineja ji raspberryje)
- [ ] fondu duomenys - https://www.swedbank.lt/private/investor/funds/allFunds/list/details
- [ ] humidity inside
- [ ] temperature out/in
- [x] log file for when was fetched and if successs or not (aisku matai in flask terminal, but anyway)
- [ ] switch one the display kai kas nors priarteja - https://tutorials-raspberrypi.com/connect-and-control-raspberry-pi-motion-detector-pir/, https://www.youtube.com/watch?v=Tw0mG4YtsZk
- [X] fix period for charts!!! make it dynamic
- [x] covid cases (not so needed and kinda hard to fetch)
- [x] population (not so needed and kinda hard to fetch)
- [x] indication, that the page has refreshed


# Docs

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