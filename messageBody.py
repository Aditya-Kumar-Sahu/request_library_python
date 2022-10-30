# `data` parameter

import requests

response = requests.post('https://httpbin.org/post', json={'key':'value'})
json_response = response.json()
print(json_response['data'])
print(json_response['headers']['Content-Type'])


# inspecting your request
print(response.request.url)
print(response.request.body)