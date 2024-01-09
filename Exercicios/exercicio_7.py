print(20*'=', 'Descubra o dobro, triplo e a raiz quadrada do valor desejado', 20*'+')
valor = int(input('Digite o valor desejado: '))
dobro = valor * 2
triplo = valor * 3
raiz = valor ** (1/2)
print('Valor dobrado: {}'.format(dobro))
print('Valor triplicado: {}'.format(triplo))
print('Raiz do valor digitado: {:.2f}'.format(raiz))
