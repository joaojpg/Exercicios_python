print(20*'=', 'Descubra a conversao de temperatura de grau celsius para fahrenheit', 20*'=')
valor = float(input('Digite o valor que deseja converter: '))
resultado = (valor * 9/5) + 32
print('A temperatura de {}°C corresponde a {}°F!'.format(valor, resultado))