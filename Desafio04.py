#serão sorteados 3 elementos entre “🍎”, “🎃”, “🍋”, “🍒”, “🤡”, caso o usuário tire 3 elementos iguais ou
# 1 elemento e 2 ou 2 elementos e um ele irá ganhar o dobro do que apostou caso ele obtenha elementos diferentes
# irá perder e caso ele tire 3 coringas ele deve ter o valor da aposta multiplicado por 3. Ao final de cada rodada
# o se o usuário ganhar pode optar por continuar e o valor da aposta será igual ao montante ganho na rodada anterior

#choice-->A sequência pode ser uma string, um intervalo, uma lista, uma tupla ou qualquer outro tipo de sequência.
import random

print("<->"*10)
print("     DESAFIO CAÇA NÍQUEL")
print("<->"*10)
listaSort=["🍎", "🎃", "🍋", "🍒", "🤡"]
print(listaSort)
print("<->"*10)

while True:
    valAposta = int(input("QUANTO DESEJA APOSTAR? "))
    print()
    st=random.choice(listaSort)
    st2=random.choice(listaSort)
    st3=random.choice(listaSort)
    print("RODANDO....")
    print()
    print("-"*30)
    print(f">>>>>{st, st2, st3}<<<<<")
    print("-"*30)

    if st == st2 == st3 == "🤡":
        valAposta = valAposta * 3
        print(f"CORINGOUUUU EMM, VOCÊ GANHOU {valAposta}R$")
    elif st == st2 == st3:
        valAposta = valAposta * 2
        print(f"TODOS IGUAIS VOCÊ GANHOU {valAposta}R$")
    elif ((st == st2) and st3 == "🤡") or ((st == st3) and st2 == "🤡") or (st == "🤡" and (st2 == st3)):
        valAposta = valAposta * 2
        print(f"2 IGUAIS E UM PALHAÇO, VOCÊ GANHOU {valAposta}R$")
    elif (st == st2 == "🤡") or (st2 == st3 == "🤡") or (st == st3 == "🤡"):
        valAposta = valAposta * 2
        print(f"2 PALHAÇOS E UM, VOCÊ GANHOU {valAposta}R$")
    else:
        print("XIII UMA SEQUÊNCIA DIFERENTE, VOCÊ PERDEU TUDO")
        quit()
    print()
    nov = input("DESEJA JOGAR NOVAMENTE? (S) <-ou-> (N) ")
    if nov == "S" or nov == "s":
        continue
    else:
        print("-"*30)
        print("     $$-FIM DE JOGO-$$")
        print(f"VOCÊ GANHOU UM TOTAL DE {valAposta}R$")
        print("-"*30)
        break




