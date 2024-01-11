import math
print(20*'=', 'Descubra a Hipotenusa de seu Triângulo Retângulo', 20*'=')
cateto1 = float(input('Digite o valor de seu Cateto Oposto: '))
cateto2 = float(input('Digite o valor de seu Cateto Adjacente: '))
resultado = cateto1 ** 2 + cateto2 ** 2
hipotenusa = math.sqrt(resultado)
print('\nHipotenusa: {}'.format(hipotenusa))
print('\nAprenda:')
print('\nPara descobrir o valor da Hipotenusa é necessário fazer a seguinte conta: Cateto Oposto ao quadrado + Cateto Adjacente ao quadrado = resultado, e com este resultado é necessário descobrir a raiz quadrada dele para obter a Hipotenusa')
print('exemplo:')
print('{}² + {}² = {}'.format(cateto1, cateto2, resultado))
print('√{} = {}'.format(resultado, hipotenusa))