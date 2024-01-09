print(20*'=', 'Descubra o desconto de uma peça de roupa de sua preferencia', 20*'=')
roupa = float(input('Digite o valor: '))
desconto = 0.05 * roupa
resultado = roupa - desconto
print('O valor total com desconto de 5% aplicado é de R${}'.format(resultado))