# invest

- [x] alphavantage - tik 25 queires KRC - https://www.alphavantage.co/documentation/
- [ ] most advanced most declined
- [ ] top gainers
- [ ] top losers
- [ ] volume
- [ ] google trends topics - https://trends.google.com/trending?geo=US
- [ ] notification when big change happened or smth like that. or simply show todays trends in telegram kaip zinute
- [x] Running eilutė kaip NASDAQe (labai trukineja ji raspberryje)
- [ ] fondu duomenys - https://www.swedbank.lt/private/investor/funds/allFunds/list/details
- [ ] humidity inside
- [ ] temperature out/in
- [ ] log file for when was fetched and if successs or not (aisku matai in flask terminal, but anyway)
- [ ] switch one the display kai kas nors priarteja - https://tutorials-raspberrypi.com/connect-and-control-raspberry-pi-motion-detector-pir/, https://www.youtube.com/watch?v=Tw0mG4YtsZk
- [ ] fix period for charts!!! make it dynamic
- [ ] covid cases
- [ ] population
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