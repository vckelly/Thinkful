import json
import requests
import authorization

from urls import *

def main():
  # main function
  auth = authorization.authorize()

  response = requests.get(TIMELINE_URL, auth=auth)
  print json.dumps(response.kson(), indent=4)
  
if __name__ == "__main__":
  main()