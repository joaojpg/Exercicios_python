vlr = int(input('Digite o ano que você deseja descobrir se é bisexto: '))

vlr1 = vlr % 4 == 0

if vlr1 == True:
    vlr2 = vlr % 100 == 0
    if vlr2 == False:
        print('O ano digitado é bisexto')
    elif vlr2 == True:
        vlr3 = vlr % 400 == 0
        if vlr3 == True:
            print('O ano digitado é bisexto')
        else:
            print('O ano digitado não é bisexto')
else:
    print('O ano digitado não é bisexto')