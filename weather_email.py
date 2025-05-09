import requests
import yagmail
import schedule
import time

API_KEY = '45daf26de3f402b52b8efdecc27e9195'
CITY = 'Chennai'  # Change to your city
EMAIL = 'pavash23@gmail.com'
EMAIL_PASSWORD = 'chbiyabvsnqrminn'  # For Gmail, use App Password

def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    weather = data['weather'][0]['description']
    temp = data['main']['temp']

    return f"Today's weather in {CITY}: {weather}, {temp}°C"

def send_email():
    yag = yagmail.SMTP(EMAIL, EMAIL_PASSWORD)
    content = get_weather()
    yag.send(to=EMAIL, subject="Daily Weather Forecast", contents=content)
    print("Email sent!")

# Schedule for every day at 8:00 AM
schedule.every().day.at("23:45").do(send_email)

while True:
    schedule.run_pending()
    time.sleep(60)