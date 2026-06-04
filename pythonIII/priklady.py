import requests

res = requests.post("http://127.0.0.1:5000/echo",json={ "moje_data" : 1111111111})

print(res.json())