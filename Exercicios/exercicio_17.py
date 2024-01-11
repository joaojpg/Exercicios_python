import math

print(20*'=', 'Descubra o numero inteiro de qualquer numero real que desejar', 20*'=')
real = float(input('Digite um valor: '))
inteiro = math.floor(real)
print('O resultado de seu valor "{}" quando inteiro é {}'.format(real, inteiro))