import math
a = float(input('Digite o comprimento do cateto oposto: '))
b = float(input('Digite o comprimento do cateto adjacente: '))
hyp = math.hypot(a, b)
print('A hipotenusa é {}'.format(hyp))
