# app/robo_advisor.py

import requests
import dotenv
import json
import datetime

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)


#
# INFO INPUTS
#

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"

response = requests.get("request_url")
#print (type(response)) #> class 'request.models.Response'>
#print (response.status_code) #>200
#print (response.text)

parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

tsd = parsed_response["Time Series (Daily)"]

# assuming latest day is first, may want to sort to ensure latest day is first
dates = list(tsd.keys())

latest_day = dtaes[0]

latest_close = tsd[latest_day]["4. close"]

breakpoint()

# get high price from each day
high_prices =[]
# maximum of all high prices
for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append(float(high_price))
recent_high = max(high_prices)


# minimum of all low prices
low_prices =[]
recent_low = min(low_prices)




#
# INFO OUTPUTS
#

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print(f"REQUEST AT:" + now.strftime("%Y-%m-%d %H:%M:%S"))
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")