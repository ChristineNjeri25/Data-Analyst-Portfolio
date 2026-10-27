import requests

# 1. The API URL (This is the "menu")
url = "https://api.open-meteo.com/v1/forecast?latitude=-1.2864&longitude=36.8172&current_weather=true"

# 2. Ask the API for the data (The "waiter")
response = requests.get(url)

# 3. Convert the response to JSON (The "food")
data = response.json()

# 4. Extract the specific data point we want
current_temp = data['current_weather']['temperature']
current_wind = data['current_weather']['windspeed']

print(f"The current temperature in Nairobi is {current_temp}°C")
print(f"The current wind speed is {current_wind} km/h")