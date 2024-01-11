from random import shuffle

print('Faça um sorteio da ordem de alunos que irão apresentar seu trabalho escolar: ')

nome1 = input('Digite o nome de seu aluno: ')
nome2 = input('Digite o nome do proximo aluno: ')
nome3 = input('Digite o nome do proximo aluno: ')
nome4 = input('Digite o nome do proximo aluno: ')
lista = [nome1, nome2, nome3, nome4]

shuffle(lista)

print('Os alunos sorteados em ordem foram:')

for ordem in lista:
    print(ordem)