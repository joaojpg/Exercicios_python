print('Descubra os centimetros e os milimetros do valor desejado: ')
valor = int(input('Digite a quantidade de metros desejados: '))
centimetros = valor * 100
milimetros = valor * 1000
print('Você digitou {} metros que são {} centimetros que são {} milimetros'.format(valor, centimetros, milimetros))