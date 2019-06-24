# app/robo_advisor.py

import json
import csv
import os

import datetime
import requests

from dotenv import load_dotenv

load_dotenv()

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

#
# INFO INPUTS
#

api_key = os.environ.get("ALPHAVANTAGE_API_KEY")

while True:
    symbol = input("Please Enter a Valid Ticker Symbol: ")

    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

    response = requests.get(request_url)

    if "Error" in response.text:
        print("This Symbol is Invalid. Please Try Again!")
        break

#print (type(response)) #> class 'request.models.Response'>
#print (response.status_code) #>200
#print (response.text)

parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

tsd = parsed_response["Time Series (Daily)"]

# assuming latest day is first, may want to sort to ensure latest day is first
dates = list(tsd.keys())

sorted_dates = sorted(dates, reverse=True)

latest_day = dates[0]

latest_close = tsd[latest_day]["4. close"]

# get high price from each day
high_prices =[]
low_prices = []
close_prices = []

# maximum of all high prices
for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append(float(high_price))
    low_price = tsd[date]["3. low"]
    low_prices.append(float(low_price))
    close_price = tsd[date]["4. close"]
    close_prices.append (float(close_price))

recent_high = max(high_prices)
recent_low = min(low_prices)
average_close = sum(close_prices)/len(close_prices)

#
# INFO OUTPUTS
#

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", f"{symbol}.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    
    for date in dates:
        daily_prices = tsd[date]
        writer.writerow({
            "timestamp": date,
            "open":  daily_prices["1. open"],
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"]
        })

#
# INFO DISPLAY
#

print("-------------------------")
print(f"SELECTED SYMBOL: {symbol}")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print(f"REQUEST AT: {now.strftime("%Y-%m-%d %H:%M:%S")}")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")

#
# RECOMMENDATION
#

if average_close > float(latest_close):
    print("RECOMMENDATION: BUY!")
    print("RECOMMENDATION REASON: The average close price is greater than the most recent close price")
else:
    print("RECOMMENDATION: SELL!")
    print("RECOMMENDATION REASON: The stock is over valued. The average close price is lower than the most recent close price")

print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}")   # use csv module
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
