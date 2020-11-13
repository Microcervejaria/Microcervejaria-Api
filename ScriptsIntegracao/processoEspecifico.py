import requests
import json

headers = {'Authorization': 'cervejaria'}
response = requests.get('https://api-homebeer.herokuapp.com/processo/fervura', headers=headers)
processo = response.json()

print(processo)
