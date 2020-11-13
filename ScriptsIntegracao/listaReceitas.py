import requests
import json

headers = {'Authorization': 'cervejaria'}
response = requests.get('https://api-homebeer.herokuapp.com/receitas', headers=headers)
listaReceitas = response.json()
receita = "Suas receitas são "
# primeiraReceita = listaReceitas[0]["nome"]
for cerveja in listaReceitas:
    receita += cerveja["nome"] + ", "

print(receita)
