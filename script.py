# the GET request
import requests

url = "https://api.github.com"
requests.get(url)
#-----------------------------------------------


# Response
response = requests.get(url)
# print(response)
#------------------------------------------------


# Status Codes
# print(response.status_code)


if response.status_code == 200:
    print("Success!")
elif response.status_code == 400:
    print("Not found. ")


if response:
    print("Success!")
else:
    print('An error has occured.')