#Um jogo no qual será sorteado um número entre 1 e 18, cada time possui 3 números que o representa,
# caso o número sorteado corresponder ao time que o usuário escolheu o usuário ganha o jogo
import random
print("*"*35)
print("TIMES A SEREM SORTEADOS: \nSANTOS - FLAMENGO - PALMEIRAS\nFORTALEZA - BOTAFOGO - CORINTHIANS")
print("*"*35)

sorteio=random.randint(1,18)
nomeTime=input("EM QUE TIME DESEJA APOSTAR? ")
if sorteio >= 1 and sorteio <= 3:
    print("O TIME SORTEADO FOI O SANTOS")
    if nomeTime == "SANTOS":
        print("PARABENS VOCÊ GANHOU")
    else:
        print("INFELIZMENTE VOCÊ PERDEU")
elif sorteio > 3 and sorteio <= 6:
    print("O TIME SORTEADO FOI O FLAMENGO")
    if nomeTime == "FLAMENGO":
        print("PARABENS VOCÊ GANHOU")
    else:
        print("INFELIZMENTE VOCÊ PERDEU")
elif sorteio > 6 and sorteio <= 9:
    print("O TIME SORTEADO FOI O PALMEIRAS")
    if nomeTime == "PALMEIRAS":
        print("PARABENS VOCÊ GANHOU")
    else:
        print("INFELIZMENTE VOCÊ PERDEU")
elif sorteio > 9 and sorteio <= 12:
    print("O TIME SORTEADO FOI O FORTALEZA")
    if nomeTime == "FORTALEZA":
        print("PARABENS VOCÊ GANHOU")
    else:
        print("INFELIZMENTE VOCÊ PERDEU")
elif sorteio > 12 and sorteio <= 15:
    print("O TIME SORTEADO FOI O BOTAFOGO")
    if nomeTime == "BOTAFOGO":
        print("PARABENS VOCÊ GANHOU")
    else:
        print("INFELIZMENTE VOCÊ PERDEU")
elif sorteio > 15 and sorteio <= 18:
    print("O TIME SORTEADO FOI O CORINTHIANS")
    if nomeTime == "CORINTHIANS":
        print("PARABENS VOCÊ GANHOU")
    else:
        print("INFELIZMENTE VOCÊ PERDEU")
