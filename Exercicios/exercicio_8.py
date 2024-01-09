print(20*'=', 'Descubra sua media', 20*'=')
portugues = int(input('Digite sua nota de Portugues: '))
matematica = int(input('Digite sua nota de Matematica: '))
ciencias = int(input('Digite sua nota de Ciencias: '))
historia = int(input('Digite sua nota de Historia: '))
geografia = int(input('Digite sua nota de Geografia: '))
media = (portugues + matematica + ciencias + historia + geografia) / 5
print('Sua media é: {}'.format(media))