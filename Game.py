import time
import random


def limparTela():          # Faz o Refresh
    print('\n' * 130)


def carregarBaralho():     # Baralho usado durante o game
    carta = ""
    for n in range(1, 5):
        if n == 1:
            naipe = "Ouro"
        elif n == 2:
            naipe = "Copa"
        elif n == 3:
            naipe = "Paus"
        elif n == 4:
            naipe = "Espada"
        for i in range(1, 14):
            if i == 1:
                carta = "A" + naipe
            elif i == 11:
                carta = "J" + naipe
            elif i == 12:
                carta = "Q" + naipe
            elif i == 13:
                carta = "K" + naipe
            else:
                carta = str(i) + naipe
            baralho.append(carta)
    random.shuffle(baralho)


def getCarta(ncarta):        # Pegar a Carta usada na vez jogada
    return baralho[ncarta]


def jogada(pontos, cartapescada, firstace):          # Distruibuição das cartas
    if cartapescada[0] == "K" or cartapescada[0] == "Q" or cartapescada[0] == "J" or cartapescada[0] == 10:
        pontos = 10
    elif cartapescada[0] == 'A':
        if firstace == 0:
            pontos = 11
        else:
            pontos = 1
    else:
        pontos = int(cartapescada[0])
    print(f"Carta: {cartapescada} Pontuação: {pontos}")
    return pontos


def linhaTracejada():      # linha com traços
    print("-" * 60)


def mostraPontuacao(nomejogador, pontosjogador, cartasjogador):
    print(f"Seu baralho: {nomejogador}   Sua pontuação: {pontosjogador}   Número de Cartas {cartasjogador}")


def verificaVencedor(wins1, wins2):
    if pontosJ1 == pontosJ2:
        print("Empate")
    elif pontosJ1 > 21:
        print(jogador2.upper() + '(J2) venceu!!')
        wins2 += 1
    elif pontosJ2 > 21:
        print(jogador1.upper() + '(J1) venceu!!')
        wins1 += 1
    elif pontosJ1 > pontosJ2:
        print(jogador1.upper() + '(J1) venceu!!')
        wins1 += 1
    elif pontosJ2 > pontosJ1:
        print(jogador2.upper() + '(J2) venceu!!')
        wins2 += 1
    print("Pontos do jogador 1:", pontosJ1,
          "Pontos do jogador 2:", pontosJ2)
    return wins1, wins2


def mostraPlacar():
    print(f"{vitoriasJ1} para {jogador1.upper()}")
    print(f"{vitoriasJ2} para {jogador2.upper()}")
    print(f"{vitoriasJ1} | {vitoriasJ2}")


def mudar(jogador):
    print("Em 6 segundos será a vez do", jogador)


baralho = []
carregarBaralho()

linhaTracejada()
print("Bem Vindo ao BlackJack!")
print("Vamos Começar!")
linhaTracejada()
time.sleep(0.5)

jogador1 = input("Escolha o nome do jogador 1: ")
linhaTracejada()
jogador2 = input("Agora, para o nome do jogador 2: ")
linhaTracejada()
while jogador1 == jogador2:
    print("Jogadores não podem ter o mesmo nome!"
          "Jogador 2 deve mudar seu nome!")
    jogador2 = input("Nome do jogador 2: ")
    linhaTracejada()

print(jogador1.upper(), "x", jogador2.upper())
print("Vamos Começar!")
time.sleep(1)

jogarNovamente = "s"
vitoriasJ1 = 0
vitoriasJ2 = 0
pescada = 0

while jogarNovamente == "s":

    pontosJ1 = 0
    cartasJ1 = 0
    firstAceJ1 = 0

    pontosJ2 = 0
    cartasJ2 = 0
    firstAceJ2 = 0

    linhaTracejada()

    # distribuir as 2 cartas iniciais para jogador 1
    linhaTracejada()
    print("Cartas Iniciais de " + jogador1.upper())
    carta = getCarta(pescada)
    pontosJ1 += jogada(pontosJ1, carta, firstAceJ1)
    if carta == "A":
        firstAceJ1 = 1
    cartasJ1 += 1
    pescada += 1

    carta = getCarta(pescada)
    pontosJ1 += jogada(pontosJ1, carta, firstAceJ1)
    if carta == "A":
        firstAceJ1 = 1
    cartasJ1 += 1
    pescada += 1
    linhaTracejada()
    mostraPontuacao(jogador1.upper(), pontosJ1, cartasJ1)
    mudar(jogador2)
    linhaTracejada()
    time.sleep(6)
    limparTela()

    # distribuir as 2 cartas iniciais para jogador 2
    linhaTracejada()
    print("Cartas Iniciais de " + jogador2.upper())
    carta = getCarta(pescada)
    if carta == "A":
        firstAceJ2 = 1
    pontosJ2 += jogada(pontosJ2, carta, firstAceJ2)
    cartasJ2 += 1
    pescada += 1

    carta = getCarta(pescada)
    pontosJ2 += jogada(pontosJ2, carta, firstAceJ2)
    if carta == "A":
        firstAceJ1 = 1
    cartasJ2 += 1
    pescada += 1
    linhaTracejada()
    mostraPontuacao(jogador2.upper(), pontosJ2, cartasJ2)
    linhaTracejada()
    mudar(jogador1)
    time.sleep(6)
    limparTela()

    # começa o jogo pelo jogador 1
    novaCarta = "s"
    while novaCarta == "s":

        if pontosJ1 >= 21 or pontosJ2 >= 21:
            break

        mostraPontuacao(jogador1.upper(), pontosJ1, cartasJ1)
        novaCarta = input(jogador1.upper() + ", deseja pegar outra carta? [S/N]")
        if novaCarta.lower() != 's':
            break

        carta = getCarta(pescada)
        pontosJ1 += jogada(pontosJ1, carta, firstAceJ1)
        if carta == "A":
            firstAceJ1 = 1
        cartasJ1 += 1
        pescada += 1

        if pontosJ1 >= 21:
            break

    linhaTracejada()
    print("Pontuaçao Final: ")
    mostraPontuacao(jogador1.upper(), pontosJ1, cartasJ1)
    if pontosJ1 < 21:
        mudar(jogador2)
        time.sleep(6)
        limparTela()
        linhaTracejada()

    # passa a vez para o jogador 2
    novaCarta = "s"
    while novaCarta == "s":

        if pontosJ1 >= 21 or pontosJ2 >= 21:
            break

        mostraPontuacao(jogador2.upper(), pontosJ2, cartasJ2)
        novaCarta = input(jogador2.upper() + ", deseja pegar outra carta? [S/N]")
        if novaCarta.lower() != 's':
            break

        carta = getCarta(pescada)
        pontosJ2 += jogada(pontosJ2, carta, firstAceJ2)
        if carta == "A":
            firstAceJ2 = 1
        cartasJ2 += 1
        pescada += 1

        if pontosJ2 >= 21:
            break

    linhaTracejada()
    print("Pontuaçao Final: ")
    mostraPontuacao(jogador2.upper(), pontosJ2, cartasJ2)
    linhaTracejada()
    time.sleep(1)

    vitoriasJ1, vitoriasJ2 = verificaVencedor(vitoriasJ1, vitoriasJ2)

    jogarNovamente = input("Vamos continuar a jogar? [S/N]").lower()
    mostraPlacar()
    time.sleep(1)
