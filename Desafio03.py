#O usuário tem 4 chances para acertar um número sorteado pela máquina entre 1 e 100, caso ele acerte
# de primeira irá ganhar o montante igual ao valor apostado acrescido de 100% (o dobro), se acertar na
# segunda tentativa irá ganhar um montante igual ao valor apostado acrescido de 50% (metade), caso ele acerte
# na terceira tentativa receberá o montante calculado por valor apostado acrescido de 25% e caso acerte na última
# receberá o valor apostado de volta.
#a. A cada rodada o sistema deve dizer se o valor é maior ou menor do que o número chutado
#b. O valor da aposta mínima é de 100,00 reais

import random
print("-"*30)
print("     JOGO DA ADIVINHAÇAO")
print("-"*30)

sort=random.randint(1, 5)
valAposta=int(input("QUANTO DESEJA APOSTAR? "))
palpite=int(input("QUAL VALOR SERÁ SORTEADO? "))
if palpite == sort:
    print(f"VOCÊ GANHOU {valAposta*2}")
elif palpite == sort:
    print(f"VOCÊ GANHOU {(valAposta+(50/100*valAposta))}")
elif palpite == sort:
    print(f"VOCÊ GANHOU {(valAposta+(25/100*valAposta))}")
else:
    print("-"*30)
    print("INFELIZMENTE, VOCÊ NÃO ACERTOU")
    print("-"*30)


