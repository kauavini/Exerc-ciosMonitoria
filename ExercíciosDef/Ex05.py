def contador(i, f, p):
	while i <= f:
		print(i)
		i += p



i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)