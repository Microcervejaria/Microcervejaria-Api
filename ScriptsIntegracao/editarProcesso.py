import requests
import json
# Aquecimento
# payload = {
#   "processo": "aquecimento",
#   "etapas": [
#       {
#           "temperatura": "70"
#       }
#   ],
#   "tempoAtual": "10",
#   "tempoRestante": "10",
#   "temperaturaAtual": "10"
# }

# Brassagem
# payload = {
#   "processo": "brassagem",
#   "etapas": [{
#     "tempo": "10",
#     "temperatura": "25",
#     "estado": "-1"
#   },{
#     "tempo": "20",
#     "temperatura": "60",
#     "estado": "1"
#   },{
#     "tempo": "60",
#     "temperatura": "10",
#     "estado": "0"
#   },{
#     "tempo": "40",
#     "temperatura": "50",
#     "estado": "0"
#   }],
#   "tempoAtual": "10",
#   "tempoRestante": "10",
#   "temperaturaAtual": "40"
# }

# Fervura
payload = {
  "processo": "fervura",
  "etapas": [{
      "ingredientes": [{
          "tempo": "10",
          "nome": "Cascade",
          "quantidade": "30",
          "unidadeMedida": "g",
          "estado": "-1"

      },{
          "tempo": "20",
          "nome": "Colungos",
          "quantidade": "30",
          "unidadeMedida": "g",
          "estado": "-1"

      },{
          "tempo": "40",
          "nome": "Herkules",
          "quantidade": "20",
          "unidadeMedida": "g",
          "estado": "-1"

      },{
          "tempo": "60",
          "nome": "Cascade",
          "quantidade": "20",
          "unidadeMedida": "g",
          "estado": "-1"

      },{
          "tempo": "60",
          "nome": "Colungos",
          "quantidade": "20",
          "unidadeMedida": "g",
          "estado": "1"

      },{
          "tempo": "70",
          "nome": "Herkules",
          "quantidade": "40",
          "unidadeMedida": "g",
          "estado": "0"

      }]
  }],
  "tempoAtual": "20",
  "tempoRestante": "10",
  "temperaturaAtual": "37"
}

headers = {'Authorization': 'cervejaria', 'Content-Type': 'application/json'}
response = requests.put('https://api-homebeer.herokuapp.com/processo',
headers=headers, data=json.dumps(payload))
processo = response.json()

print(processo)
