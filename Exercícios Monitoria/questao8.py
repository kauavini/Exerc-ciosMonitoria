fact = int(input('Digite um valor para saber seu factorial: '))
p = 1
c = fact
while c > 0:
    print('{} '.format(c), end='')
    print('x ' if c > 1 else '= ', end='')
    p *= c
    c -= 1
print('{}'.format(p), end='')
