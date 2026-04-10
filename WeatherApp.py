import requests
# API = '7fa1ff114ef904c9cb8686e4f7a21753'

city = input('Enter a city: ')


api_key = '7fa1ff114ef904c9cb8686e4f7a21753'
url = 'https://api.openweathermap.org/data/2.5/weather'

info = {
    'q': city,
    'appid': api_key,
    'units': 'metric',
}

fetch = requests.get(url, params=info)

if fetch.status_code == 200:
    print(fetch.json())
else:
    print('Fetch Error:', fetch.status_code)

data = fetch.json()

temp = data['main']['temp']
weather_description = data['weather'][0]['description']
humidity = data['main']['humidity']

print(f'The temperature in {city} is {temp} degrees Celsius, and the humidity is {humidity}.')
print(f'The weather is {weather_description}.')