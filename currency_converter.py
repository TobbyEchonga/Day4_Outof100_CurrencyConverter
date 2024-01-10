import requests

def get_exchange_rate(api_key, base_currency, target_currency):
    url = f"https://open.er-api.com/v6/latest/{base_currency}"
    params = {
        "apikey": api_key
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        rates = data['rates']
        if target_currency in rates:
            return rates[target_currency]
        else:
            return None
    else:
        return None

def convert_currency(amount, exchange_rate):
    if exchange_rate is not None:
        converted_amount = amount * exchange_rate
        return converted_amount
    else:
        return None

# Replace 'YOUR_API_KEY' with your actual API key from Open Exchange Rates
api_key = 'YOUR_API_KEY'
base_currency = input("Enter base currency (e.g., USD): ").upper()
target_currency = input("Enter target currency (e.g., EUR): ").upper()
amount = float(input("Enter amount to convert: "))

exchange_rate = get_exchange_rate(api_key, base_currency, target_currency)

if exchange_rate is not None:
    converted_amount = convert_currency(amount, exchange_rate)
    print(f"{amount} {base_currency} equals {converted_amount:.2f} {target_currency}")
else:
    print("Failed to fetch exchange rates or invalid currency.")
