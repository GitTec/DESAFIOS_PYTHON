import random

nSorteados = []
nEscolhidos = []
cont = 0
ap=0

valAposta = float(input("QUAL VALOR DESEJA APOSTAR? "))
if valAposta >= 50 and valAposta <= 100:
    while ap < 4:
        aposta1 = int(input(f"ESCOLHA 4 NÚMEROS: "))
        ap += 1
        nEscolhidos.append(aposta1)
elif valAposta >= 101 and valAposta <= 150:
    while ap < 5:
        aposta2 = int(input("ESCOLHA 5 NÚMEROS: "))
        ap += 1
        nEscolhidos.append(aposta2)
elif valAposta >= 151:
    while ap < 6:
        aposta3 = int(input("ESCOLHA 6 NÚMEROS: "))
        ap += 1
        nEscolhidos.append(aposta3)
else:
    print("VALOR DA APOSTA NÃO É ACEITO!!")
nEscolhidos.sort()
print("-"*25)
print(f"SEU JOGO: {nEscolhidos}")
print("-"*25)

for i in range(51):
    numSorteio = random.randint(1, 50)
    if numSorteio not in nSorteados:
        nSorteados.append(numSorteio)
        cont += 1
    if cont >= 6:
        break

print("-" * 50)
nSorteados.sort()
print(f"NÚMEROS SORTEADOS: {nSorteados}")
print("-" * 50)

for i in nSorteados:
    if i in nEscolhidos:
        print(f"VOCÊ ACERTOU OS NÚMEROS: ", i, end=" ")






