import requests

url = "http://127.0.0.1:5500/hotovo.csv"

response = requests.get(url)

print(response.status_code)   # 201 = Created
print(response.text)        # odpoveď s uloženým objektom


