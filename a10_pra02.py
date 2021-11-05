print('AULA 10 - CONDIÇÕES I')

print('\nDIÁRIO DIGITAL DO PROFESSOR')
av1 = float(input('Informe a nota da prova 1: '))
av2 = float(input('Informe a nota da prova 2: '))
media = (av1 + av2)/2
print('\n= A média é {:.2f}. ' .format(media), end='')
print('Poxa, você está reprovado!' if media <= 6 else 'Parabéns, você está aprovado!')
