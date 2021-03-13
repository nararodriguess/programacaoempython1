largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura: '))
area = largura*altura
print (f'Sua parede possui dimensão de {largura}x{altura} e sua area é de {area} metro(s) quadrado(s).', end=' ')
print(f'É necessário {area/2} lata(s) de tinta.')
