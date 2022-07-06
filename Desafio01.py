#Um jogo no qual será sorteado um número entre 1 e 18, cada time possui 3 números que o representa,
# caso o número sorteado corresponder ao time que o usuário escolheu o usuário ganha o jogo
import random
print("*"*35)
print("TIMES A SEREM SORTEADOS: \nSANTOS - FLAMENGO - PALMEIRAS\nFORTALEZA - BOTAFOGO - CORINTHIANS")
print("*"*35)

sorteio=random.randint(1,18)

if sorteio == 1 and sorteio <= 3:
    print("O TIME SORTEADO FOI O SANTOS")
elif sorteio > 3 and sorteio <= 6:
    print("O TIME SORTEADO FOI O FLAMENGO")
elif sorteio > 6 and sorteio <= 9:
    print("O TIME SORTEADO FOI O PALMEIRAS")
elif sorteio > 9 and sorteio <= 12:
    print("O TIME SORTEADO FOI O FORTALEZA")
elif sorteio > 12 and sorteio <= 15:
    print("O TIME SORTEADO FOI O BOTAFOGO")
elif sorteio > 15 and sorteio <= 18:
    print("O TIME SORTEADO FOI O CORINTHIANS")
