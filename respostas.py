import requests
import telebot
import time

from jsons import id_jogadas, pegar_resultado, last_number
from mensagens import mensagem_red_green, mensagens_gale
from env import Chat_id, Api_token

bot = telebot.TeleBot(Api_token)


def blaze():
    resposta = requests.get("https://blaze-7.com/api/roulette_games/recent")
    return resposta.text


def telegram(texto):
    bot.send_message(Chat_id, texto)


def atualizar_numeros():
    resposta = blaze()
    id_jogada = id_jogadas(resposta, 1)
    tempo_jogar(id_jogada)
    resposta = blaze()
    ultimo_numero = last_number(resposta, 1)
    return ultimo_numero


def atualizar():
    resposta = blaze()
    id_jogada = id_jogadas(resposta, 1)
    tempo_jogar(id_jogada)
    resposta = blaze()
    lista_resultado = pegar_resultado(resposta, 1)
    return lista_resultado


def tempo_jogar(ids):
    while True:
        resposta = blaze()
        jogadas = id_jogadas(resposta, 1)
        if jogadas != ids:
            print("Nova rodada!")
            break


def resposta_preto():
    lista_resultado = atualizar()
    print(lista_resultado)
    resposta = blaze()
    if lista_resultado == ['Preto']:
        telegram(mensagem_red_green("green"))
        print(mensagem_red_green("green"))
        return "green"

    elif lista_resultado == ['Vermelho']:
        telegram(mensagens_gale(resposta, "Preto", 1))
        print(mensagens_gale(resposta, "Preto", 1))

        # Confimar RED ou GREEN NO GALE
        time.sleep(1)
        lista_resultado = atualizar()
        print(lista_resultado)

        if lista_resultado == ['Preto']:
            telegram(mensagem_red_green("green"))
            print(mensagem_red_green("green"))
            return "green"

        elif lista_resultado == ['Vermelho']:
            telegram(mensagens_gale(resposta, "Preto", 2))
            print(mensagens_gale(resposta, "Preto", 2))

            time.sleep(1)
            lista_resultado = atualizar()
            print(lista_resultado)

            if lista_resultado == ['Preto']:
                telegram(mensagem_red_green("green"))
                print(mensagem_red_green("green"))
                return "green"

            elif lista_resultado == ['Vermelho']:
                telegram(mensagem_red_green("red"))
                print(mensagem_red_green("red"))
                return "red"

            elif lista_resultado == ['Branco']:
                telegram(mensagem_red_green("green"))
                print(mensagem_red_green("green"))
                return "green"

        elif lista_resultado == ['Branco']:
            telegram(mensagem_red_green("green"))
            print(mensagem_red_green("green"))
            return "green"

    elif lista_resultado == ['Branco']:
        telegram(mensagem_red_green("green"))
        print(mensagem_red_green("green"))
        return "green"


def resposta_vermelho():
    lista_resultado = atualizar()
    print(lista_resultado)
    resposta = blaze()
    if lista_resultado == ['Vermelho']:
        telegram(mensagem_red_green("green"))
        print(mensagem_red_green("green"))
        return "green"

    elif lista_resultado == ['Preto']:
        telegram(mensagens_gale(resposta, "Vermelho", 1))
        print(mensagens_gale(resposta, "Vermelho", 1))

        # Confimar RED ou GREEN NO GALE
        time.sleep(1)
        lista_resultado = atualizar()
        print(lista_resultado)

        if lista_resultado == ['Vermelho']:
            telegram(mensagem_red_green("green"))
            print(mensagem_red_green("green"))
            return "green"

        elif lista_resultado == ['Preto']:
            telegram(mensagens_gale(resposta, "Vermelho", 2))
            print(mensagens_gale(resposta, "Vermelho", 2))

            time.sleep(1)
            lista_resultado = atualizar()
            print(lista_resultado)

            if lista_resultado == ['Vermelho']:
                telegram(mensagem_red_green("green"))
                print(mensagem_red_green("green"))
                return "green"

            elif lista_resultado == ['Preto']:
                telegram(mensagem_red_green("red"))
                print(mensagem_red_green("red"))
                return "red"

            elif lista_resultado == ['Branco']:
                telegram(mensagem_red_green("green"))
                print(mensagem_red_green("green"))
                return "green"

        elif lista_resultado == ['Branco']:
            telegram(mensagem_red_green("green"))
            print(mensagem_red_green("green"))
            return "green"

    elif lista_resultado == ['Branco']:
        telegram(mensagem_red_green("green"))
        print(mensagem_red_green("green"))
        return "green"
