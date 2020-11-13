import requests
import json

headers = {'Authorization': 'cervejaria'}
payload={'nomeReceita': ""}
response = requests.post('https://api-homebeer.herokuapp.com/limpeza', headers=headers, data=payload)
serverResponse = response.json()
if not 'erro' in serverResponse:
    speak_output = serverResponse["message"]
else:
    speak_output = "Seu token é inválido, por favor adicione um token válido para continuar"

print(speak_output)
