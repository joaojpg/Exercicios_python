from random import choice

print('Faça um sorteio de alunos para ter um selecionado que possa apagar o quadro por você')
nome1 = input('Digite o nome de seu aluno: ')
nome2 = input('Digite o nome do proximo aluno: ')
nome3 = input('Digite o nome do proximo aluno: ')
nome4 = input('Digite o nome do proximo aluno: ')
lista = [nome1, nome2, nome3, nome4]
print('O aluno sorteado foi o {}!'.format(choice(lista)))