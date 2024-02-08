import json


def id_jogadas(resposta, numbers):
    lista_resu = []
    json_valores = json.loads(resposta)
    for index, valores in enumerate(json_valores):
        if index < numbers:
            lista_resu.append(valores["id"])
    return lista_resu


def pegar_resultado(resposta, numbers):
    lista_resultados = []
    json_valores = json.loads(resposta)
    for valores in json_valores:
        if valores["color"] == 1:
            valores["color"] = "Vermelho"

        elif valores["color"] == 2:
            valores["color"] = "Preto"

        elif valores["color"] == 0:
            valores["color"] = "Branco"
    for index, valores in enumerate(json_valores):
        if index < numbers:
            lista_resultados.append(valores["color"])
    return lista_resultados


def last_number(resposta, number):
    lista_last = []
    json_valor = json.loads(resposta)
    for index, valores in enumerate(json_valor):
        if index < number:
            lista_last.append(valores["roll"])
    return lista_last

