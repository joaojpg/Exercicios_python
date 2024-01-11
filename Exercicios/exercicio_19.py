import math

print('Descubra o Seno, Cosseno e Tangente do angulo desejado')
angulo = float(input('Digite o valor do angulo: '))
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)
print('Estes são os valores:\nSeno: {:.3f}\nCosseno: {:.3f}\nTangente: {:.3f}'.format(seno, cosseno, tangente))