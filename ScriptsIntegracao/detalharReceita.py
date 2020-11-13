import requests
import json

headers = {'Authorization': 'cervejaria'}
pedido_receita = 'taguatinga ipa'
response = requests.get('https://api-homebeer.herokuapp.com/receitas', headers=headers)
listaReceitas = response.json()
if not 'erro' in listaReceitas:
    lista =[]
    for cerveja in listaReceitas:
        lista.append(cerveja["nome"].lower())
    if pedido_receita not in lista:
        speak_output = "Você não possui esta receita em sua Micro cervejaria, se quiser pergunte por sua lista de receitas"
    else:
        url = 'https://api-homebeer.herokuapp.com/receitas?nome_like=' + pedido_receita
        response = requests.get(url, headers=headers)
        receita = response.json()[0]
        ingredientes = ""
        for i in receita['ingredientes']:
            ingredientes += F"{i['nome']} {i['quantidade']} {i['unidadeMedida']}. "

        brassagem = ""
        for i in receita['brassagem']:
            brassagem +=  F"{i['temperatura']} graus célsius, por {i['tempo']} minutos. "

        fervura = ""
        for i in receita['fervura']['ingredientes']:
            fervura += F"{i['quantidade']} {i['unidadeMedida']} de {i['nome']} serão adicionados aos {i['tempo']} minutos. "

        speak_output = F"""\
        A cerveja {receita['nome']} é uma {receita['descricao']}. \
        Seu tempo médio de produção é de {receita['tempoMedio']} minutos e produz {receita['quantidadeLitros']} litros. \
        Os ingredientes utilizados são: {ingredientes}\
        Durante sua fase de aquecimento, a cerveja é aquecida a uma temperatura de {receita['aquecimento']['temperatura']} graus célsius. \
        Durante a brassagem, será realizado os seguintes degraus de aquecimento:  A temperatura vai ficar em {brassagem} \
        A fervura vai durar um tempo total de {receita['fervura']['tempoTotal']} minutos. E os seguintes ingredientes vão ser adicionados: {fervura}\
        """
else:
    speak_output = "Seu token é inválido, por favor adicione um token válido para continuar"

print(speak_output)
# print(teste)
