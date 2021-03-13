print('>'*15,'<'*15)
intro = '\033[7;41mJOGO DA ADIVINHAÇÃO\033[m'
print(f'{intro:^40}')
print('>'*15, '<'*15)

from time import sleep
sleep(1)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')

print(' ')
sleep(3)

from random import randint
computador= randint(0,5)
v = int(input('Qual é o numero que você acha que eu pensei? '))
print('Loanding...')
sleep(1)
if v == computador:
    print('PARABÉNS, VOCÊ GANHOU!!!')
else:
    print(f'Não foi dessa vez! Eu pensei em {computador} e não em {v}. GAME OVER!')
