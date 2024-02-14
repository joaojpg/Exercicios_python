#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('Descubra se as retas digitadas podem formar um triangulo.')
print('Para que seja possivel fazer um triangulo é necessario que os dois menores valores somados sejam maiores do que o maior valor.')
print('Exemplos:\n2, 3, 10 Com este valor não é possivel fazer um triangulo pois a soma dos dois menores valores é menor do que o maior valor')
print('2, 3, 5 Com este valor tambem não é possivel pois a soma dos dois menores valores é igual ao maior valor e com isso seria formada uma linha, não um triangulo')
print('3, 3, 5 Com este valor é possivel fazer um triangulo pois a soma dos dois menores valores passam o maior valor!')

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

maior = max(a, b, c)

if maior == a:
    resultado = a < b + c

elif maior == b:
    resultado = b < a + c

elif maior == c:
    resultado = c < a + b

if resultado:
    print('Com estes valores {}, {}, {} é possivel fazer um triangulo!'.format(a, b, c))

else:
    print('Com estes valores {}, {}, {} não é possivel fazer um triangulo!'.format(a, b, c))