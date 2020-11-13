import requests
import json

headers = {'Authorization': 'cervejaria'}
payload = {
    "nome": "Taguatinga IPA",
    "descricao": "Cerveja com sabor Taguatinguense",
    "tempoMedio": "180",
    "quantidadeLitros": "50",
        "ingredientes": [{
                "nome": "Água",
                "quantidade": "21",
                "unidadeMedida": "Litros"
            },
            {
                "nome": "Malte Pielsen",
                "quantidade": "5",
                "unidadeMedida": "Kilos"
            },
            {
                "nome": "Malte Melanoidina",
                "quantidade": "1",
                "unidadeMedida": "Kilos"
            },
            {
                "nome": "Lúpulo Herkules",
                "quantidade": "20",
                "unidadeMedida": "gramas"
            },
            {
                "nome": "Lúpulo Cascade",
                "quantidade": "80",
                "unidadeMedida": "gramas"
            },
            {
                "nome": "Lúpulo Columbus",
                "quantidade": "80",
                "unidadeMedida": "gramas"
            },
            {
                "nome": "Fermento US05",
                "quantidade": "1",
                "unidadeMedida": "pacote"
            }
        ],
    "aquecimento": {
        "temperatura": "90"
    },
        "brassagem": [{
                "tempo": "60",
                "temperatura": "80"
            },
            {
                "tempo": "15",
                "temperatura": "85"
            }
        ],
        "fervura": {
            "tempoTotal": "60",
            "ingredientes": [{
                    "tempo": "60",
                    "nome": "Herkules",
                    "quantidade": "20",
                    "unidadeMedida": "gramas"
                },
                {
                    "tempo": "10",
                    "nome": "Columbus",
                    "quantidade": "30",
                    "unidadeMedida": "gramas"
                },
                {
                    "tempo": "5",
                    "nome": "Cascade",
                    "quantidade": "30",
                    "unidadeMedida": "gramas"
                },
                {
                    "tempo": "0",
                    "nome": "Cascade",
                    "quantidade": "20",
                    "unidadeMedida": "gramas"
                },
                {
                    "tempo": "0",
                    "nome": "Columbus",
                    "quantidade": "20",
                    "unidadeMedida": "gramas"
                }
            ]
    }
    }
response = requests.post('https://api-homebeer.herokuapp.com/receita', headers=headers, data=payload)

print(response)
