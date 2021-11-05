print('\033[7;40m AULA 12 - CONDIÇÕES ANINHADAS \033[m')
import emoji

genre = str(input('\n\033[1mQual teu gênero musical predileto? \033[m')).strip().casefold()

if genre == 'mpb' or genre == 'rock':
    print('\033[1;35mBacana!')
elif genre == 'classica' or genre == 'jazz' or genre == 'blues':
    print('\033[1;32mNão tão comum...\033[m')
elif genre in 'funk pop trap':
    print(emoji.emojize('\033[1;36mGosta de agito, né!:? :man_dancing:\033[m', use_aliases=True))
else:
    print('\033[1;33mInteressante, não conhecia!\033[m')