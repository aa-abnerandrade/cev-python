print('\033[1;7;40m AULA 16: TUPLAS \033[m\n')

names = ('Tony', 'Maria', 'Ana', 'Sofia', 'José', 'João', 'André')

print('*** Colocando em ordem* com SORTED:')
print(sorted(names))
print('* nesse caso, ordem alfabética'.rjust(50))
print('*** Mas note que:'
      '\nTuplas são IMUTÁVEIS!!!'
      f'\n{names}')

print('\nE se observar ainda mais, os () foram substiuídos por [] quando colocamos em SORTED')
print('Isso porque o Python transformou a TUPLA em LISTA')