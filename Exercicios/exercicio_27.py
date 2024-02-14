#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

print('Descubra aonde esta a primeira e a ultima letra a de seu texto')
text = str(input('Digite seu texto: ').upper().strip())

text1 = text.find('A') + 1
text2 = text.rfind('A') + 1

print('No seu texto a primeira ocorrencia da letra "A" é em {} e a ultima ocorrencia é em {}'.format(text1, text2))