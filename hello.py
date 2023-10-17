import requests
def test():

  url = "http://localhost:5000/test"

  payload={}
  headers = {}

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)

test()