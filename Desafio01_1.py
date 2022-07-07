import random

sorteio = random.randint(1,19)

while True:
    timeSorteado = ""
    nomeTime = input("EM QUAL TIME DESEJA JOGAR? ")
    if sorteio >= 1 and sorteio <=3:
        timeSorteado = "SANTOS"
    elif sorteio > 3 and sorteio <=6:
        timeSorteado = "FLAMENGO"
    elif sorteio > 6 and sorteio <=9:
        timeSorteado = "PALMEIRAS"
    elif sorteio > 9 and sorteio <= 12:
        timeSorteado = "FORTALEZA"
    elif sorteio > 12 and sorteio <=15:
        timeSorteado = "BOTAFOGO"
    elif sorteio > 15 and sorteio <= 18:
        timeSorteado = "CORINTHIANS"

    print(f"O TIME SORTEADO FOI O {timeSorteado}")

    if nomeTime != timeSorteado:
        print("-"*30)
        print("VOCÊ PERDEU, INFORME OUTRO TIME")
        print("-" * 30)
    else:
        print("-" * 30)
        print("PARABÉNS!!! VOCÊ GANHOU")
        print("-"*30)
        break