import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API = "Your own API Key"
STOCK_API = "Your own API Key"

Account_SID = "Your Twilio account SID"
Auth_token = "Your Twilio account token"

parameters = {
    "function":"TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "apiKey": STOCK_API
}

resource = requests.get(url= STOCK_ENDPOINT, params= parameters)
resource.raise_for_status()  #check status
data = resource.json()["Time Series (Daily)"] 

data_list = [value for (key,value) in data.items]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday["4. close"]

difference =day_before_yesterday_closing_price - yesterday_closing_price

up_down = None
if up_down >0 :
    up_down = "🔺"
else:
    up_down = "🔻"

percent = round((difference / float(yesterday_closing_price)) * 100)

if abs(percent) > 4:
    parameters_news = {
        "apiKey": NEWS_API,
        "qInTitle": COMPANY_NAME,
    }
    news_resource = requests.get(url = NEWS_ENDPOINT, params = parameters_news)
    news_resource.raise_for_status()
    articles = news_resource.json()["articles"]
    three_articles = articles[:3]
    formatted_list = [f"Headline: {articles['title']}\n Brief: {articles['description']}" for article in three_articles]

    client = Client(Auth_token, Account_SID)
    for article in formatted_list:
        client.messages.create(
            body = article,
            from_= "+18154291795",
            to = "Your verified phone number."
        )




