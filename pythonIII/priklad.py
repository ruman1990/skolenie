import requests

url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)
data = response.json()
print(data)
# Výstup: {'userId': 1, 'id': 1, 'title': '...', 'completed': False}