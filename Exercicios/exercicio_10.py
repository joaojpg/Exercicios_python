print(20*'=', 'Descubra a tabuada do numero desejado', 20*'=')
numero = int(input('Digite um valor: '))
var = 1
resultado = numero * var
while var < 11:
    print('{} x {} = {}'.format(numero, var, resultado))
    var += 1
    resultado = numero * var