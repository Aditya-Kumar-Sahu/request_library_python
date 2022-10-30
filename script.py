# the GET request
import requests

url = "https://api.github.com"
requests.get(url)


# Response
response = requests.get(url)
print(response)