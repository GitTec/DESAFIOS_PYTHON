import random

nSorteados = []
nEscolhidos = []
cont = 0
ap=0

valAposta = float(input("QUAL VALOR DESEJA APOSTAR? "))
if valAposta >= 50 and valAposta <= 100:
    while ap < 4:
        aposta1 = int(input(f"ESCOLHA O {ap+1}° NÚMERO: "))
        if aposta1 > 50:
            print("ERRO!- INFORME VALOR ENTRE 1 e 50")
            continue
        ap += 1
        nEscolhidos.append(aposta1)
elif valAposta >= 101 and valAposta <= 150:
    while ap < 5:
        aposta2 = int(input(f"ESCOLHA O {ap+1}° NÚMERO: "))
        if aposta2 > 50:
            print("ERRO!- INFORME VALOR ENTRE 1 e 50")
            continue
        ap += 1
        nEscolhidos.append(aposta2)
elif valAposta >= 151:
    while ap < 6:
        aposta3 = int(input(f"ESCOLHA O {ap+1}° NÚMERO: "))
        if aposta3 > 50:
            print("ERRO!- INFORME VALOR ENTRE 1 e 50")
            continue
        ap += 1
        nEscolhidos.append(aposta3)
else:
    print("VALOR DA APOSTA NÃO É ACEITO!!")
    quit()
nEscolhidos.sort()
print("-"*25)
print(f"SEU JOGO: {nEscolhidos}")
print("-"*25)

while cont < 6:
    numSorteio = random.randint(1, 50)
    if numSorteio not in nSorteados:
        nSorteados.append(numSorteio)
        cont += 1

print("-" * 50)
nSorteados.sort()
print(f"NÚMEROS SORTEADOS: {nSorteados}")
print("-" * 50)

cont=0
for i in nSorteados:
    if i in nEscolhidos:
        cont +=1
print(f"VOCÊ ACERTOU {cont} NÚMERO(S)")
print("-"*30)
#print(f"VOCÊ ACERTOU OS NÚMEROS: ", i, end=" ")

if cont == 0:
    print("VOCÊ PERDEU TUDO")
elif cont == 1:
    print(f"APOSTOU {valAposta:.2f}R$ E GANHOU {valAposta + (valAposta / 2):.2f}R$")
elif cont == 2:
    print(f"APOSTOU {valAposta:.2f}R$ E GANHOU {valAposta*2:.2f}R$")
elif cont == 3:
    print(f"APOSTOU {valAposta:.2f}R$ E GANHOU {valAposta**2:.2f}R$")
elif cont == 4:
    print(f"APOSTOU {valAposta:.2f}R$ E GANHOU {valAposta**3:.2f}R$")
elif cont == 5:
    print(f"APOSTOU {valAposta:.2f}R$ E GANHOU {valAposta**4:.2f}R$")
else:
    print(f"VOCÊ GANHOU 1 MILHÃO DE R$")
print("-"*30)





