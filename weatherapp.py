import requests


api_key = '9648f1632430cf8903a72db2cd477118'
user_input = input('enter city name:')

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

data = weather_data.json()

if 'weather' in data:
    weather = data['weather'][0]['main']
    temp = round(data['main']['temp'])
    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}°F")
else:
    print("Error: Weather data not found.")
    print(data)  # to see what the response was
