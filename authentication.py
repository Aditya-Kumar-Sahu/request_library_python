# Authentication helps a service understand who you are. 
# Typically, you provide your credentials to a server by 
# passing data through the Authorization header or a custom 
# header defined by the service. All the request functions 
# you’ve seen to this point provide a parameter called auth, 
# which allows you to pass your credentials.



# from requests.auth import HTTPBasicAuth

# from getpass import getpass
# import requests
# print(requests.get(
#     'https://api.github.com/user',
#     auth=HTTPBasicAuth('username', getpass())))



# to supply your own authentication mechanism
import requests
from requests.auth import AuthBase

class TokenAuth(AuthBase):
    """Implements a custom authentication scheme."""

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        """Attach an API token to a custom auth header."""
        r.headers['X-TokenAuth'] = f'{self.token}'  # Python 3.6+
        return r


print(requests.get('https://httpbin.org/get', auth=TokenAuth('12345abcde-token')))