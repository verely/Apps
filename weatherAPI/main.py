import requests
import smtplib
import os

my_api = os.environ.get('WEATHER_API')
myLat = 31.850680
myLon = 34.838980
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
weather_params = {
    "lat": myLat,
    "lon": myLon,
    "appid": my_api,
    "exclude": "current,minutely,daily,alerts",
    "units": "metric"
}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

data = response.json()
weather_data_slice = data["hourly"][:12]
print(weather_data_slice)

temp = []
wind = []
humidity = []
will_rain = False
dust_alert_on = False
for hour_data in weather_data_slice:
    temp.append(hour_data["temp"])
    wind.append(hour_data["wind_speed"])
    humidity.append(hour_data["humidity"])
    condition_id = hour_data["weather"][0]["id"]
    if condition_id == 731 or condition_id < 751:
        dust_alert_on = True
    if condition_id < 600:
        will_rain = True

max_temp = max(temp)
min_temp = min(temp)
max_wind = max(wind)
min_wind = min(wind)
max_humidity = max(humidity)
min_humidity = min(humidity)
msg = f"Weather conditions for following 12 hours\n Temperature: {min_temp}/{max_temp}\n Wind: {min_wind}/{max_wind}" \
      f"\n Humidity: {min_humidity}/{max_humidity}"
if max_temp > 32 and dust_alert_on:
    msg += "It is a Khamsin, don't forget to bring a bottle of water and to close the windows at home"
if will_rain:
    msg += "It will rain, don't forget to bring an umbrella"

print(msg)

bot_email = os.environ.get('BOTMAIL')
bot_password = os.environ.get('BOTPASS')
recipient = "valery_voinova@hotmail.com"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=bot_email, password=bot_password)
    connection.sendmail(from_addr=bot_email,
                        to_addrs=recipient,
                        msg=f"Subject: weather today\n\n {msg}")
