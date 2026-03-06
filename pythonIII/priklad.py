import requests

url = 'https://www.nasa.gov/wp-content/uploads/2023/06/jwst-flickr-52259221868-30e1c78f0c-4k.jpg?w=2048'
response = requests.get(url)

with open('obrazok.jpg', 'wb') as f:
    f.write(response.content)