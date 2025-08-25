import requests

url = "http://localhost:5000/add"
payload = {"a": 5, "b": 7}

response = requests.post(url, json=payload)
print(response.json())   # {"result": 12}