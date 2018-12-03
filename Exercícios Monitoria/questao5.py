n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1
valorinicial = menor + 1
while valorinicial <= maior - 1:
    print(valorinicial)
    valorinicial += 1
