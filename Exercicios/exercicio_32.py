print('Descubra o valor de sua passagem pela distancia!')
distancia = int(input('Digite a distancia em km: '))

if distancia <= 200:
    resultado1 = 0.50 * distancia
    print('O valor de sua passagem ficou {:.2f}'.format(resultado1))
else:
    resultado2 = 0.45 * distancia
    print('O valor de sua passagem ficou {:.2f}'.format(resultado2))
