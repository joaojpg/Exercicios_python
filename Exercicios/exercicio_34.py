print('Digite 3 numeros e descubra qual é o maior e qual é o menor')
vlr = int(input('Digite o primeiro valor: '))
vlr1 = int(input('Digite o segundo valor: '))
vlr2 = int(input('Digite o terceiro valor: '))
menor = vlr
maior = vlr

if vlr1 < vlr and vlr1 < vlr2:
    menor = vlr1
if vlr2 < vlr and vlr2 < vlr2:
    menor = vlr2

if vlr1 > vlr and vlr1 > vlr2:
    maior = vlr1
if vlr2 > vlr1 and vlr2 > vlr:
    maior = vlr2

print('Este é o menor valor digitado: {}'.format(menor))

print('Este é o maior valor digitado {}'.format(maior))