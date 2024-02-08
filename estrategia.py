from respostas import blaze, telegram, resposta_preto, resposta_vermelho
from mensagens import mensagens_entrada, porcentagem
from jsons import pegar_resultado


def estrategia4color():
    # Estratégias
    resposta = blaze()
    estrategia1 = ['Vermelho', 'Vermelho', 'Vermelho', 'Vermelho']  # Cair Preto
    estrategia2 = ['Preto', 'Preto', 'Preto', 'Preto']  # Cair Vermelho
    lista_resultados = pegar_resultado(resposta, 4)

    # Enviar Estratégias
    if lista_resultados == estrategia2:
        print("estrategia4color")
        telegram(mensagens_entrada(resposta, "Vermelho"))
        print(mensagens_entrada(resposta, "Vermelho"))

        # Confirmar RED or GREEN
        jogada = resposta_vermelho()
        if jogada == "green":
            resu = porcentagem("green")
            print(resu)
            telegram(resu)
        elif jogada == "red":
            resu = porcentagem("red")
            print(resu)
            telegram(resu)

    # Enviar Estratégias
    elif lista_resultados == estrategia1:
        print("estrategia4color")
        telegram(mensagens_entrada(resposta, "Preto"))
        print(mensagens_entrada(resposta, "Preto"))

        # Confirmar RED or GREEN
        jogada = resposta_preto()
        if jogada == "green":
            resu = porcentagem("green")
            print(resu)
            telegram(resu)
        elif jogada == "red":
            resu = porcentagem("red")
            print(resu)
            telegram(resu)


def estrategiaBranco():
    # Estratégias
    resposta = blaze()
    estrategia1 = ['Branco', 'Vermelho']
    estrategia2 = ['Branco', 'Preto']
    lista_resultados = pegar_resultado(resposta, 2)

    # Enviar Estratégias
    if lista_resultados == estrategia2:
        print("estrategiaBranco")
        telegram(mensagens_entrada(resposta, "Vermelho"))
        print(mensagens_entrada(resposta, "Vermelho"))

        # Confirmar RED or GREEN
        jogada = resposta_vermelho()
        if jogada == "green":
            resu = porcentagem("green")
            print(resu)
            telegram(resu)
        elif jogada == "red":
            resu = porcentagem("red")
            print(resu)
            telegram(resu)

    # Enviar Estratégias
    elif lista_resultados == estrategia1:
        print("estrategiaBranco")
        telegram(mensagens_entrada(resposta, "Preto"))
        print(mensagens_entrada(resposta, "Preto"))

        # Confirmar RED or GREEN
        jogada = resposta_preto()
        print("Resultado foi:", jogada)
        if jogada == "green":
            resu = porcentagem("green")
            print(resu)
            telegram(resu)
        elif jogada == "red":
            resu = porcentagem("red")
            print(resu)
            telegram(resu)


def estrategia_dentada():
    # Estratégias
    estrategia1 = ['Vermelho', 'Preto', 'Vermelho', 'Preto', 'Vermelho', 'Preto', 'Vermelho']
    estrategia2 = ['Preto', 'Vermelho', 'Preto', 'Vermelho', 'Preto', 'Vermelho', 'Preto']
    resposta = blaze()
    lista_resul = pegar_resultado(resposta, 7)

    # Verificar se entra na estratégia
    if lista_resul == estrategia1:
        print("estrategia_dentada")
        telegram(mensagens_entrada(resposta, "Vermelho"))
        print(mensagens_entrada(resposta, "Vermelho"))

        # Verificar se vai dar vermelho
        jogada = resposta_vermelho()

        if jogada == "green":
            resu = porcentagem("green")
            print(resu)
            telegram(resu)
        elif jogada == "red":
            resu = porcentagem("red")
            print(resu)
            telegram(resu)

    # Verificar se entra na estratégia
    elif lista_resul == estrategia2:
        print("estrategia_dentada")
        telegram(mensagens_entrada(resposta, "Preto"))
        print(mensagens_entrada(resposta, "Preto"))

        # Verificar se vai dar vermelho
        jogada = resposta_preto()

        if jogada == "green":
            resu = porcentagem("green")
            print(resu)
            telegram(resu)
        elif jogada == "red":
            resu = porcentagem("red")
            print(resu)
            telegram(resu)


def estrategiaTeste():
    # Estratégias
    resposta = blaze()
    estrategia1 = ['Vermelho']
    estrategia2 = ['Preto']
    lista_resultado = pegar_resultado(resposta, 1)

    # Enviar Estratégia 1
    if lista_resultado == estrategia1:
        print("estrategiaTeste")
        telegram(mensagens_entrada(resposta, "Vermelho"))
        print(mensagens_entrada(resposta, "Vermelho"))

        # Confirmar RED or GREEN de primeira
        jogada = resposta_vermelho()

        if jogada == "green":
            resu = porcentagem("green")
            print(resu)
            telegram(resu)
        elif jogada == "red":
            resu = porcentagem("red")
            print(resu)
            telegram(resu)

    # Enviar Estratégia 2
    elif lista_resultado == estrategia2:
        print("estrategiaTeste")
        telegram(mensagens_entrada(resposta, "Preto"))
        print(mensagens_entrada(resposta, "Preto"))

        # Confirmar RED or GREEN de primeira
        jogada = resposta_preto()
        if jogada == "green":
            resu = porcentagem("green")
            print(resu)
            telegram(resu)
        elif jogada == "red":
            resu = porcentagem("red")
            print(resu)
            telegram(resu)
