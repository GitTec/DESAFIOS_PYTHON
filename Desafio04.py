#serão sorteados 3 elementos entre “🍎”, “🎃”, “🍋”, “🍒”, “🤡”, caso o usuário tire 3 elementos iguais ou
# 1 elemento e 2 ou 2 elementos e um ele irá ganhar o dobro do que apostou caso ele obtenha elementos diferentes
# irá perder e caso ele tire 3 coringas ele deve ter o valor da aposta multiplicado por 3. Ao final de cada rodada
# o se o usuário ganhar pode optar por continuar e o valor da aposta será igual ao montante ganho na rodada anterior

#choice-->A sequência pode ser uma string, um intervalo, uma lista, uma tupla ou qualquer outro tipo de sequência.

print("<->"*10)
print("     DESAFIO CAÇA NÍQUEL")
print("<->"*10)
listaSort=["🍎", "🎃", "🍋", "🍒", "🤡"]
print(listaSort)
print("<->"*10)

import random
st=random.choice(listaSort)
st2=random.choice(listaSort)
st3=random.choice(listaSort)
print("RODANDO....")
print("")
print("-"*30)
print(f">>>>>{st, st2, st3}<<<<<")
print("-"*30)
#valGanho=[]

while True:
    valAposta = int(input("QUANTO DESEJA APOSTAR? "))
    print()
    if st == st2 == st3 == "🤡":
        ganho=(print(f"CORINGOUUUU EMM, VOCÊ GANHOU {valAposta * 3}"))
 #       valGanho.append(ganho)
    if st == st2 == st3:
        ganho2=(print(f"TODOS IGUAIS VOCÊ GANHOU {valAposta * 2}R$"))
  #      valGanho.append(ganho2)
    elif st == st2:
        ganho3=(print(f"2 PRIMEIROS IGUAIS, VOCÊ GANHOU {valAposta * 2}R$"))
   #     valGanho.append(ganho3)
    elif st2 == st3:
        ganho4=(print(f"2 ÚLTIMOS IGUAIS, VOCÊ GANHOU {valAposta * 2}R$"))
    #    valGanho.append(ganho4)
    else:
        print("XIIIII UMA SEQUÊNCIA DIFERENTE, VOCÊ PERDEU TUDO")
        quit()
    print()
    nov = input("DESEJA JOGAR NOVAMENTE? (S) <-ou-> (N) ")
    if nov == "S" or nov=="s":
        continue
    else:
        print("$$-FIM DE JOGO-$$")
     #   print(f"VOCÊ GANHOU {sum(valGanho)}")
        break




