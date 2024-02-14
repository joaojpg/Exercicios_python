from random import randint

print('Vamos brincar :)')
print('Descubra em que numero eu estou pensando entre 0 a 5')
numero = int(input('Digite: '))
computador = randint(0, 5)

if numero == computador:
    print('Parabens, você acertou!')
else:
    print('Que pena você errou, eu pensei no numero {}, tente novamente!'.format(computador))
input('Aperte "ENTER" para finalizar o programa.')