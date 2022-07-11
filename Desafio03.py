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

valSort=random.randint(1, 5)
valAposta=int(input("QUANTO DESEJA APOSTAR? "))
print("-"*30)

vez = 0
while vez < 3:
    palpite = int(input("CHUTE UM VALOR? "))
    vez += 1

    if palpite < valSort:
        print(f"O VALOR É MAIOR QUE {palpite}")
    elif palpite > valSort:
        print(f"O VALOR É MENOR QUE {palpite}")
    elif vez > 4:
        print("INFELIZMENTE ACABARAM AS CHANCES, VOCÊ PERDEU!!!")

        if palpite == valSort:
            print(f"PARABÉNS!!! VOCÊ GANHOU {valAposta * 2}R$")
        elif palpite == valSort:
            print(f"PARABÉNS!!! VOCÊ GANHOU {(valAposta + (50 / 100 * valAposta))}R$")
        elif palpite == valSort:
            print(f"PARABÉNS!!! VOCÊ GANHOU {(valAposta + (25 / 100 * valAposta))}R$")
        break



