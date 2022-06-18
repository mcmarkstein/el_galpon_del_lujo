import requests

url = "https://api.apilayer.com/exchangerates_data/convert?to=ARS&from=EUR&amount=150"

payload = {}
headers= {
  "apikey": "2fmmJ7Dlc4Wuh2XTDemrC75HYq9Zc9eQ"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.json

print(result)




