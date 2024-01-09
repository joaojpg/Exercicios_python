#Estou considerando que U$1,00 = R$3,27

print(20*'=', 'Conversor de reais para dolares: ', 20*'=')
valor = float(input('Digite um valor: '))
resultado = valor / 3.27
print('A conversão da U${:.2f}'.format(resultado))