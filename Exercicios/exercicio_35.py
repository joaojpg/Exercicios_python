#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

print('Descubra quanto vai ser o seu aumento salarial!')
salario = float(input('Digite o seu salario: '))

if salario >= 1250:
    vlr_maior = 0.10 * salario
    vlr_maior_r = vlr_maior + salario
    print('Seu salario com o aumento de 10% vai passar de {:.2f} para {:.2f}, parabéns!'.format(salario, vlr_maior_r))
else:
    vlr_menor = 0.15 * salario
    vlr_menor_r = vlr_menor + salario
    print('Seu salario com o aumento de 15% vai passar de {:.2f} para {:.2f}, parabéns!'.format(salario, vlr_menor_r))