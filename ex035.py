print('-'*40)
intro = 'ANALISANDO UM TRIANGULO'
print(f'\033[33m{intro:^40}\033[m')
print('-'*40)
a = float(input('Digite a medida do lado A do triangulo: '))
b = float(input('Digite a medida do lado B do triângulo: '))
c = float(input('Digite a medida do lado C do triângulo: '))
if a <= b + c and b <= a + c and c <= a +b:
    print('\033[0:32mÉ possivel criar um triangulo com essas medidas.')
else:
    print('\033[0:31mNão é possivel criar um triangulo com essas medidas')
