print(20*'=', 'Descubra o valor de seu salario com o aumento de 15%', 20*'=')
valor = float(input('Digite o valor: '))
aumento = 0.15 * valor
resultado = valor + aumento
print('O valor total com desconto de 15% aplicado é de R${}'.format(resultado))