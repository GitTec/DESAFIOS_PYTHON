#serão sorteados 6 números de 1 até 50, o usuário recebe a premiação de acordo com a quantidade
# de acertos, segue abaixo a tabela. O usuário pode fazer uma aposta no valor entre 50,00 e 100,00
# que dará direito a escolher 4 números, ele pode apostas 101,00 até 150,00 que dará direito a escolher
# 5 números e apostas maiores que 151,00 dará direito a 6 números

import random
nSorteados=[]
nEscolhidos=[]
cont=0

while True:
    valAposta=float(input("QUAL VALOR DESEJA APOSTAR? "))

    if valAposta >= 50 and valAposta <= 100:
        aposta1 = int(input("ESCOLHA 4 NÚMEROS: "))
        nEscolhidos.append(aposta1)
    elif valAposta >= 101 and valAposta <= 150:
        aposta2= int(input("ESCOLHA 5 NÚMEROS: "))
        nEscolhidos.append(aposta2)
    elif valAposta >= 151:
        aposta3= int(input("ESCOLHA 6 NÚMEROS: "))
        nEscolhidos.append(aposta3)
    else:
        print("VALOR DA APOSTA NÃO É ACEITO!!")
    print(nEscolhidos)

    numSorteio = random.randint(1,50)
    if numSorteio not in nSorteados:
        nSorteados.append(numSorteio)
        cont += 1
    if cont >= 6:
        break
print("-"*50)
print(f"NÚMEROS SORTEADOS: {nSorteados}")
print("-"*50)
