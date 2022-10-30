# to cutomize headers

# For example, you can change your previous search request to highlight 
# matching search terms in the results by specifying the text-match 
# media type in the Accept header.

import requests

response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)

# View the new `text-matches` array which provides information
# about your search term within the results
json_response = response.json()
repository = json_response['items'][0]
print(f'Text matches: {repository["text_matches"]}')

'''
The Accept header tells the server what content types your application can handle.
'''