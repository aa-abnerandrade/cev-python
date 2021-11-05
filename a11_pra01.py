print('=' * 9, 'AULA 11 - CORES NO TERMINAL', '=' * 9)

cores = {'clean': '\033[m',
                'atention': '\033[1;31;40m',
                'ok': '\033[4;30;42m',
                'baw': '\033[40;7m'}

print()
print(cores['baw'], '  STYLE   ', ' TXT COLOR   ', '  BG COLOR', cores['clean'])

print('\033[0m      None    ', '\033[0;30m  Black       ', '        \033[0;30;47m Grey \033[m')
print('\033[0m      None    ', '\033[0;31m  Red         ', '        \033[0;31;46m Cyan \033[m')
print('\033[1m      Bold    ', '\033[1;32m  Green       ', '        \033[1;32;45m Magenta \033[m')
print('\033[1m      Bold    ', '\033[1;33m  Yellow        ', '      \033[1;33;44m Blue \033[m')
print('\033[4m  Underline  ', '\033[1;34m  Blue      ', '       \033[1;34;43m Yellow \033[m')
print('\033[4m  Underline  ', '\033[1;35m  Magenta', '      \033[1;35;42m Green \033[m')
print('\033[7m  Negative   ', '\033[1;36m  Cyan          ', '       \033[1;36;41m Red \033[m')  # O negative inverte cor do texto e cor do background
print('\033[7m  Negative   ', '\033[1;37m  Grey          ', '      \033[1;37;40m Black \033[m')  # O negative inverte cor do texto e cor do background
print()

print('\n\033[7;40;1mComo abrir/fechar o comando de cor: " \ 0 3 3 [ ; -  ; - - ; - - m " \033[m')
