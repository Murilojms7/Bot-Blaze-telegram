from datetime import datetime
from jsons import last_number


def mensagens_entrada(resposta, color):
    if color == "Vermelho":
        return f"🧨Entrada Confirmada!🧨 \n Data: {hora()} Hora: {mins()} \n Game: Double Blaze \n Entrada: Vermelho🔴🔴🔴 \n Proteger: Branco⚪⚪⚪ \n Ultimo foi: {last_number(resposta, 1)}"
    elif color == "Preto":
        return f"🧨Entrada Confirmada!🧨 \n Data: {hora()} Hora: {mins()} \n Game: Double Blaze \n Entrada: Preto⚫⚫⚫ \n Proteger: Branco⚪⚪⚪ \n Ultimo foi: {last_number(resposta, 1)}"


def mensagens_gale(resposta, cor, number):
    if cor == "Vermelho":
        if number == 1:
            return f"🪄Vamos para o GALE 1🪄 \n Data: {hora()} Hora: {mins()} \n Double Blaze \n Entrada: Vermelho🔴🔴🔴 \n Proteger: Branco⚪⚪⚪ Ultimo foi: {last_number(resposta, 1)}"

        elif number == 2:
            return f"🪄Vamos para o GALE 2🪄 \n Data: {hora()} Hora: {mins()} \n Double Blaze \n Entrada: Vermelho🔴🔴🔴 \n Proteger: Branco⚪⚪⚪ Ultimo foi: {last_number(resposta, 1)}"

    elif cor == "Preto":
        if number == 1:
            return f"🪄Vamos para o GALE 1🪄 \n Data: {hora()} Hora: {mins()} \n Double Blaze \n Entrada: Preto⚫⚫⚫  \n Proteger: Branco⚪⚪⚪ Ultimo foi: {last_number(resposta, 1)}"

        elif number == 2:
            return f"🪄Vamos para o GALE 2🪄 \n Data: {hora()} Hora: {mins()} \n Double Blaze \n Entrada: Preto⚫⚫⚫  \n Proteger: Branco⚪⚪⚪ Ultimo foi: {last_number(resposta, 1)}"


# Green e Red
acertos = [0, 0]


def porcentagem(redOUgreen):
    if redOUgreen == 'green':
        acertos[0] += 1
    elif redOUgreen == 'red':
        acertos[1] += 1
    return f"{acertos[0]} 🟢 / {acertos[1]} 🔴 / Total: {acertos[0] + acertos[1]}"


def mensagem_red_green(color):
    if color == "red":
        return ("🔴RED!🔴")

    elif color == "green":
        return ("🟢GREEN!🟢")


def hora_aposta():
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")
    print(data_e_hora_em_texto)


def hora():
    data_e_hora_atuais = datetime.now()
    horas = data_e_hora_atuais.strftime("%d/%m/%Y")
    return horas


def mins():
    data_e_hora_atuais = datetime.now()
    minutos = data_e_hora_atuais.strftime("%H:%M")
    return minutos
