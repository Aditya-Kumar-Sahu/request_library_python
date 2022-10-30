# to customize a GET request, pass values through query string
from urllib import response
import requests

# Search GitHub's repositories for requests
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q':'requests+language:python'},        # pasing dictionary
    # params=[('q', 'requests+language:python')],     # passing list of tuples
    # params=b'q'='requests+language:python'          # passing bytes
)

# Inspect some attributes of the `requests` repositiory
json_response = response.json()
repository = json_response['items'][0]
print(f"Repository name: {repository['name']}")
print(f"Repository description: {repository['description']}")

'''
Query strings are useful for parameterizing GET requests. 
You can also customize your requests by adding or modifying the headers you send.
'''