# the GET request
import http
import requests

# requests.get("https://api.github.com")
#-----------------------------------------------



# Response
# response = requests.get("https://api.github.com")
# print(response)
#------------------------------------------------



# Status Codes
# print(response.status_code)


# if response.status_code == 200:
#     print("Success!")
# elif response.status_code == 400:
#     print("Not found. ")


# if response:
#     print("Success!")
# else:
#     print('An error has occured.')
#-------------------------------------------------



# small code 1
# # import requests
# from requests.exceptions import HTTPError

# for url in ["https://api.github.com", "https://api.github.com/invalid"]:
#     try:
#         response = requests.get(url)

#         # If the reesponse was successful, no Exception will be raised
#         response.raise_for_status()
#     except HTTPError as http_err:
#         print(f"HTTP error occurred: {http_err}")   # Python 3.6
#     except Exception as err:
#         print(f"Other error occured: {err}")    # Python 3.6
#     else:
#         print('Success!')
#--------------------------------------------------



# Content
response = requests.get("https://api.github.com")
print(response.content)
print("\n")

print(response.text)
print("\n")

response.encoding = "utf-8"     # Optional: requests infer this internally
print(response.text)
print("\n")

print(response.json())