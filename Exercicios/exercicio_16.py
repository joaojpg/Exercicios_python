print(20*'=', 'Descubra o valor que deve ser pago pelo aluguel do carro', 20*'=')
valor1 = float(input('Digite a quantidade de km percorridos com o carro: '))
valor2 = float(input('Digite a quantidade de dias que você ficou com o carro: '))
resultado = valor1 * 0.15 + valor2 * 60
print('O aluguel a ser pago é R${}'.format(resultado))