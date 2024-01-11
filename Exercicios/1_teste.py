import math
import emoji

print(emoji.emojize('Programa de importação teste :thumbs_up:'))
print('Descubra a raiz quadrada do valor desejado')
num = int(input('Digite um valor: '))
raiz = math.sqrt (num)
print('Este é a raiz de {} é {:.3f}' .format(num, raiz))