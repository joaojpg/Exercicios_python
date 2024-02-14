print('Descubra quantas unidades, dezenas, centenas e unidades tem no numero digitado!')
numero = int(input('Digite no maximo 4 numeros: '))
num = str(numero)
numero_cont = len(num)

if numero_cont == 4:
    print('Esta é sua milhar: ', num[0])
    print('Esta é sua centena: ', num[1])
    print('Esta é sua dezena: ', num[2])
    print('Esta é sua unidade: ', num[3])

elif numero_cont == 3: 
    print('Esta é sua centena: ', num[0])
    print('Esta é sua dezena: ', num[1])
    print('Esta é sua unidade: ', num[2])

elif numero_cont == 2:
    print('Esta é sua dezena: ', num[0])
    print('Esta é sua unidade: ', num[1])

elif numero_cont == 1:
    print('Esta é sua unidade: ', num[0])

else:
    print('Erro: o valor precisa ter no maximo 4 caracteres')
