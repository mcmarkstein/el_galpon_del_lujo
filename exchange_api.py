import requests
url = "https://api.apilayer.com/exchangerates_data/convert?to=ARS&from={tipo_de_cambio}&amount={precio}".format(tipo_de_cambio = 'EUR', precio = '150')
payload = {}
headers = {
    "apikey": "2fmmJ7Dlc4Wuh2XTDemrC75HYq9Zc9eQ"
}
response = requests.request("GET", url, headers=headers, data=payload)

rsps_json = response.json()

print(rsps_json["result"])

{
  'success': True,
 'query': {'from': 'EUR', 'to': 'ARS', 'amount': 150},
 'info': {'timestamp': 1655584263, 'rate': 129.265183},
 'date': '2022-06-18',
 'result': 19389.77745
 }