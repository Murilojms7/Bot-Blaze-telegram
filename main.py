from estrategia import estrategiaBranco, estrategia_dentada, estrategia4color, estrategiaTeste
from respostas import atualizar

if __name__ == "__main__":
    while True:
        print("Analizando entradas...")
        lista_resultado = atualizar()
        if not estrategia4color():
            if not estrategiaBranco():
                if not estrategia_dentada():
                    if not estrategiaTeste():
                        pass
