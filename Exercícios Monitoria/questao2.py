lista = []
for i in range(5):
	lista.append(int(input('Digite um valor: ')))
maior = lista[0]
for i in range(5):
	if lista[i] > maior:
		maior = lista[i]
print(maior)
