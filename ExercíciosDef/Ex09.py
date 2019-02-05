def CalcularAluguel(d , km):
	return 60.0 * d + km * 0.15


print('R$',CalcularAluguel(int(input('Dias: ')), int(input('Km rodados: '))))
