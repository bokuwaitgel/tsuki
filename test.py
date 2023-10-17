import requests
import os
url = "https://dev.mazaal.ai/api/sdk/pre-trained-models/22"
url_out = "https://dev.mazaal.ai/api/sdk/pre-trained-models/output/22?outId="
# def MazaalToRequest(file ):
#     payload={'prompt': 'what year is it'}
#     files=[
#     ('image',('test.png',open('./test.png', 'rb'),'image/png'))
#     ]
#     headers = {
#     'Authorization': 'mz-787925a6-60b6-4e2d-9f9b-5fdc67fa4c9c'
#     }

#     response = requests.request("POST", url, headers=headers, data=payload, files=files)

#     print(response.text)


def MazaalToRequest(filename, prompt):

    payload={'prompt': prompt}
    files = [
    ('image', (filename, open('./images/'+filename, 'rb'), 'image/png'))
    ]
    
    headers = {
    'Authorization': 'mz-787925a6-60b6-4e2d-9f9b-5fdc67fa4c9c'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    return response.text
  
def GetResult(id):
  headers = {
    'Authorization': 'mz-787925a6-60b6-4e2d-9f9b-5fdc67fa4c9c'
  }
  response = requests.request("GET", url_out+id, headers=headers)
  data = response.json()
  res =  data['output']['output']
  result = ''
  
  for i in range(len(res)):
    result += res[i]+' '

  return result