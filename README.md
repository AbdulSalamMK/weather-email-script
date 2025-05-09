# 🌤️ Weather Email Script

This Python script fetches the current day's weather forecast from OpenWeatherMap and sends it to your Gmail inbox every morning at **8:00 AM** automatically.

---

## 🚀 Features

- 🌦️ Real-time weather forecast using OpenWeatherMap API  
- 📧 Sends forecast via Gmail using yagmail  
- ⏰ Automatically scheduled with Python's `schedule` module  
- 🔐 Uses Gmail App Password for secure sending  

---

## 🛠️ Requirements

```bash
pip install requests schedule yagmail
```

---

## ⚙️ Setup Instructions

1. **Edit the script (`weather_email.py`) and update:**

```python
API_KEY = 'your_openweathermap_api_key'
CITY = 'YourCity'
EMAIL = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_app_password'
```

2. **Run the script:**

```bash
python weather_email.py
```

3. The script runs continuously and sends the email every morning at 8:00 AM.

---

## 🔐 Gmail App Password Setup

If using Gmail, enable [2-Step Verification](https://myaccount.google.com/security) and create an [App Password](https://myaccount.google.com/apppasswords).  
Use that app password in `EMAIL_PASSWORD`.

---

## 📦 Example Output

**Email Subject:**  
`Daily Weather Forecast`

**Email Body:**  
`Today's weather in <Your City> : clear sky, 29.4°C`

---

## 👨‍💻 Author

**AbdulSalamMK** – Freelance Python Developer 🇮🇳🇸🇬  
[GitHub](https://github.com/AbdulSalamMK)

---

## ⭐️ Show Your Support

If you found this useful, give it a ⭐️ on GitHub!
