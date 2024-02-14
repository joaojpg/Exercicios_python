#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
print('Descubra se o nome de sua cidade começa com "Santo"')
cidade = input("Digite o nome de sua cidade: ").strip()
print(cidade[:5].upper() == 'SANTO')
