print('Digite qualquer valor e descubra informações a respeito de seu tipo de dados')
tipos = input('Digite: ')
print('Este valor tem o tipo de dado', type(tipos))
print('Este valor é um valor numerico?', tipos.isnumeric())
print('Este valor é totalmente em maiusculos?', tipos.isupper())
print('Este valor é decimal?', tipos.isdecimal())
print('Este valor é alphanumerico?', tipos.isalpha())
print('Este valor é minusculo?', tipos.islower())