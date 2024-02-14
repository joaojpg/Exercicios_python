print('Formatando letras!')
nome =  input('Digite seu nome completo: ')
nome_tratado = nome.replace(' ', '')
nome_tratado_2 = nome.split()

print('Este é seu nome com todas as letras maiusculas: ', nome.upper())
print('Este é seu nome com todas as letras minusculas: ', nome.lower())
print('Seu nome sem espaços tem essa quantidade de letras: ', len(nome_tratado))
print('Esta é a contagem de letras do seu primeiro nome: ', len(nome_tratado_2[0]))