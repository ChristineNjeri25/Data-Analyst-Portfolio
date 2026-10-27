import requests

# 1. The API URL (No key required!)
url = "https://open.er-api.com/v6/latest/USD"

# 2. Get the data
response = requests.get(url)
data = response.json()

# 3. Extract the Kenyan Shilling rate
kes_rate = data['rates']['KES']

print(f"1 US Dollar = {kes_rate} Kenyan Shillings")