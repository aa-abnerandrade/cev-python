import emoji
print('AULA 09 - CONDIÇÕES I')

time = int(input('\nQuanto tempo tem seu veículo (em anos): '))
if time <= 5:
    print(emoji.emojize('\n:police_car: Caramba, seu veículo é novo! :police_car:', use_aliases=True))
else:
    print(emoji.emojize('\nVamos trocar de carro? :money_with_wings: ', use_aliases=True))

#Forma Simplificada de IF ELSE
print('CARRO NOVO' if time <= 5 else 'CARRO VELHO')
