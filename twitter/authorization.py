import urlparse
import requests
from requests_oauthlib import OAuth1

from secret import CLIENT_KEY, CLIENT_SECRET
from urls import *

def get_request_token():
  # get a token allowing us to request user authorization
  oauth = OAuth1(CLIENT_KEY, client_secret = CLIENT_SECRET)
  response = requests.post(REQUEST_TOKEN_URL, auth = oauth)
  credentials = urlparse.parse_qs(response.content)
  
  request_token = credentials.get("oauth_token")[0]
  request_secret = credentials.get("oauth_token_secret")[0]
  return request_token, request_secret

def get_user_authorization(request_token):
  # redirect the user to authorize the client, and get them to give us the verification code
  authorize_url = AUTHORIZE_URL
  authorize_url = authorize_url.format(request_token=request_token)
  print 'Please go here and authorize: ' + authorize_url
  return raw_input('Please input the verifier: ')

def get_acess_token(request_token, request_secret, verifier):
  # get a token which will allow us to make requests to the API
  oauth = OAuth1(CLIENT_KEY, 
                client_secret=CLIENT_SECRET,
                resource_owner_key=request_token,
                resource_owner_secret=request_secret, 
                verifier=verifier)
  
  response = requests.post(ACCESS_TOKEN_URL, auth=oauth)
  credentials = urlarese.parse_qs(response.content)
  access_token = credentials.get('oauth_token')[0]
  access_secret = credentials.get('oauth_token_secret')[0]
  return access_token, access_secret

def authorize():
  #A complete OAuth authentication flow
  request_token, request_secret = get_request_token()
  verifier = get_user_authorization(request_token)
  access_token, access_secret = get_access_token(request_token, 
                                                request_secret,
                                                verifier)
  oauth = OAuth1(CLIENT_KEY,
                client_secret=CLIENT_SECRET,
                 resource_owner_key=access_token,
                 resource_owner_secret=access_secret)
  return oauth