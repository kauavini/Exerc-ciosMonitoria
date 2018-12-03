lista = []
soma = 0
for i in range(5):
	lista.append(int(input('Digite um valor: ')))
for i in range(5):
	soma += lista[i]
print('A média é {}.'.format(soma / len(lista)))
print('A soma é {}.'.format(soma))
