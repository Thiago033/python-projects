from    dotenv      import load_dotenv
from    twilio.rest import Client
from    newsapi     import NewsApiClient
import  requests
import  os

load_dotenv()

STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
MY_NUMBER = os.getenv("MY_NUMBER")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

#Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
stock_data = response.json()

daily_stock_data = stock_data["Time Series (Daily)"]

#Get yesterday's closing stock price.
data_stock_list = [value for (key, value) in daily_stock_data.items()]
yesterday_closing_price = data_stock_list[0]["4. close"]

#Get the day before yesterday's closing stock price.
day_before_yesterday_closing_price = data_stock_list[1]["4. close"]

#Find the positive difference between 1 and 2.
stocks_difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if stocks_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#The percentage difference in price between closing price yesterday and closing price the day before yesterday.
difference_percent = round((stocks_difference / float(yesterday_closing_price)) * 100)

#Use https://newsapi.org/ 
# if percentage is greater than 5 use the News API to get articles related to the COMPANY_NAME, get the first 3 news pieces for the COMPANY_NAME. 

#*************************
#UNCOMMENT THIS             
#*************************
if abs(difference_percent) > 5:
    news_parameters = {
        "apikey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }

    response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    news_data = response.json()
    articles = news_data["articles"]

    first_three_articles = articles[:3]

    formatted_articles = [f"{STOCK_NAME}: {up_down}{difference_percent}%\nHeadline: {article['title']}\nDescription: {article['description']}" for article in first_three_articles]

    #Use twilio.com/docs/sms/quickstart/python
    #send a separate message with each article's title and description to your phone number. 
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=TWILIO_PHONE_NUMBER,
            to=MY_NUMBER
        )

        print(message.status)
