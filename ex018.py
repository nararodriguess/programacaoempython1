from math import radians, sin, cos, tan
a = float(input('Digite o valor do angulo: '))
print(f'O seno é {sin(radians(a)):.2f} o cosseno é {cos(radians(a)):.2f} e a tangente é {tan(radians(a)):.2f}.')

import math
print('O seno é {:.2f} o cosseno é {:.2f} e a tangente é {:.2f}'.format(math.sin(math.radians(a)), math.cos(math.radians(a)), math.tan(math.radians(a))))
