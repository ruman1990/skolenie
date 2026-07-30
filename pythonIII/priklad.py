import requests

resp = requests.get("https://105666b0f4.cbaul-cdnwnd.com/42839cfecaef64999df7f82ca41cd2c1/200000010-f2b19f30a3-public/[obrazky.4ever.sk]+havo+9466572.jpg")
print(resp.status_code)
print(resp.headers)

with open("web_obrazok.jpg","wb") as f:
    f.write(resp.content)
