import random

while True:
    acao_usuario = input("Escolha uma opção (pedra, papel, tesoura): ")

    acoes_possiveis = ["pedra", "papel", "tesoura"]

    acao_computador = random.choice(acoes_possiveis)

    print(f"\nVocê escolheu {acao_usuario}, o computador escolheu {acao_computador}.\n")

    if acao_usuario == acao_computador:
        print("Ambos jogadores escolheram " + acao_usuario + ". Empate!")

    elif acao_usuario == "pedra":
        if acao_computador == "tesoura":
            print("Pedra esmaga a tesoura! Você ganhou!")
        else:
            print("Papel cobre pedra! Você perdeu.")

    elif acao_usuario == "papel":
        if acao_computador == "pedra":
            print("Papel cobre pedra! Você ganhou!")
        else:
            print("Tesoura corta papel! Você perdeu.")

    elif acao_usuario == "tesoura":
        if acao_computador == "papel":
            print("Tesoura corta papel! Você ganhou!")
        else:
            print("Pedra esmaga tesoura! Você perdeu.")

    jogar_novamente = input("Jogar novamente? (s/n): ")
    if jogar_novamente.lower() != "s":
        break