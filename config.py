from datetime import datetime, timedelta

# Stock data
end_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1)
start_date = end_date - timedelta(days=366)
SYMBOLS = ["TSLA", "TM", "AAPL", "BTC-USD", "MSFT"]
HISTORICAL_URL = "https://query1.finance.yahoo.com/v7/finance/download/"
START_DATE_UNIX = int(start_date.timestamp())
START_DATE_HUMAN = start_date.strftime('%Y-%m-%d')
END_DATE_UNIX = int(end_date.timestamp())
END_DATE_HUMAN = end_date.strftime('%Y-%m-%d')

# CVBankas
CVBANKAS_KEYWORDS = ["django", "pkc"]
