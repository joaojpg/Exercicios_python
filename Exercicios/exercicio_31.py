print('Descubra se seu numero é par ou impar')
valor = int(input('Digite o valor: '))
resultado = valor % 2 == 0

if resultado == True:
    print('Seu numero "{}" é PAR!'.format(valor))

else:
    print('Seu numero "{}" é IMPAR!'.format(valor))
