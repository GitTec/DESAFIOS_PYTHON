import random

cartas=["K", "Q", "J"]
carSort=[]

escolha=int(input("EM QUAL CARTA ESTÁ A DAMA? [1] - [2] - [3] "))
cont=0
while cont < 3:
    sortCart = random.choice(cartas)
    if sortCart not in carSort:
        carSort.append(sortCart)
        cont += 1
print("-"*15)
print(carSort)
print("-"*15)

if escolha == 1 and carSort[len(carSort[0])-1] == "Q":
    print("PARABÉNS VOCÊ ACHOU A DAMA!!!")
elif escolha == 2 and carSort[len(carSort[1])] == "Q":
    print("PARABÉNS VOCÊ ACHOU A DAMA!!!")
elif escolha == 3 and carSort[len(carSort)-1] == "Q":
    print("PARABÉNS VOCÊ ACHOU A DAMA!!!")
else:
    print("X"*35)
    print("PERDEU!! VOCÊ NAO ACHOU A DAMA")
    print("X" * 35)