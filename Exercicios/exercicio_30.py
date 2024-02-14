print('Descubra se você foi multado!')

vlc = int(input('Digite a velocidade que você passou no radar: '))

if vlc > 80:
    multa = ((vlc - 80) * 7) + 300
    print('Você foi multado!')
    print('Sua multa foi no valor de R$:{}'.format(multa))
else:
    print('Você não foi multado!')
