#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
print('Você tem silva no nome?')
cidade = str(input('Digite seu nome completo: ')).upper().strip()

cidade1 = cidade.find('SILVA')

print(cidade1 >= 0)