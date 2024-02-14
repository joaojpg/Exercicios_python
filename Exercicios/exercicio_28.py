#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome completo: ').strip())
nome1 = nome.split()

print('Seu primeiro nome é {} e seu ultimo nome é {}.'.format(nome1[0], nome1[-1]))
