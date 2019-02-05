def CalcularSegundo(d, h, s):
	return (86.400 * d) + (3600 * h) + s


print(CalcularSegundo(int(input('Dias: ')), int(input('Horas: ')), int(input('Segundos: '))))

