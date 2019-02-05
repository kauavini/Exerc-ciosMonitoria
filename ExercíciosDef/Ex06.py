def TempodeVida(cpd, a):
	return ((a * 365 * cpd) * 10) / 24


from math import trunc
cpd = int(input('Quantos cigarros vc fuma por dia? '))
a = int(input('Há quantos anos vc fuma? '))
diasperdidos = TempodeVida(cpd, a)
print('Dias perdidos: {}'.format(trunc(diasperdidos)))


