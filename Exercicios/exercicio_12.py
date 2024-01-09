# Um litro de tinta pode pintar 2m²

print(20*'=', 'Descubra a área de sua parede e quantos litros de tinta serão necessarios para pintar por completo', 20*'=')
largura = float(input('Digite a largura de sua parede: '))
altura = float(input('Digite a altura de sua parede: '))
area = largura * altura
tinta = area / 2
print('A area de sua parede é {}m², supondo que um litro de tinta pode pintar 2m² será necessario {} litros de tinta'.format(area, tinta))