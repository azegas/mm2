# invest

- [x] alphavantage - tik 25 queires KRC - https://www.alphavantage.co/documentation/
- [ ] most advanced most declined
- [ ] top gainers
- [ ] top losers
- [ ] volume
- [ ] google trends topics - https://trends.google.com/trending?geo=US
- [ ] notification when big change happened or smth like that. or simply show todays trends in telegram kaip zinute
- [ ] Running eilutė kaip NASDAQe
- [ ] fondu duomenys - https://www.swedbank.lt/private/investor/funds/allFunds/list/details
- [ ] humidity inside
- [ ] temperature out/in
- [ ] log file for when was fetched and if successs or not (aisku matai in flask terminal, but anyway)


# Docs

Connect to pi from windows:
```pwsh
ssh arvypi@raspberrypi.local
```

Copy all files(excluding some folders) to the pi
```pwsh
tar --exclude-vcs -czf - -C . . | ssh arvypi@raspberrypi.local "tar -xzvf - -C /home/arvypi/Desktop/invest-scp"
```
