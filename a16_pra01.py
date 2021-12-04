print('\033[1;7;40m AULA 16: TUPLAS \033[m\n')

names = ('Tony', 'Maria', 'Ana', 'Sofia', 'José', 'João', 'André')

print('*** ALGUNS FATIAMENTOS: ')
print(f'Nome na posição 3: {names[3]}')
print(f'Nome na posição -3: {names[-3]}')
print(f'Na posição 6: {names[6]}')
print(f'Nomes nas posições 1 a 3: {names[1:3+1]}')
print(f'De 2 até o final da tupla: {names[2:]}')
print(f'Do início até a posição 2: {names[:2]}')
print(f'Na posição -1: {names[-1]}')
print(f'Importante lembrar que lemos da esquerda pra direita mesmo em intervalo negativo: {names[-4:-2+1]}')
print('\n*** LEMBRANDO:')
print(f'Quantidade de itens nessa tupla: {len(names)}')

print('\n\033[1;7;40m TRABALHANDO COM FOR \033[m')

print('\n*** Da maneira que vimos até aqui: ')
for cont in range(1, 3+1):
    print(f'{names} contagem: {cont}')

print('\n*** Utilizando o LEN')
for cont in range(0, len(names)):
    print(f'Nome: {names[cont]} | Posição: {cont}')
print('O zero nesse caso é o que permite a visualização completa! ')

print('\n*** Utilizando a TUPLA como RANGE:')
for cont in names:
    print(f'Meu nome é {cont}')
print('Dessa forma é possível fazer muito mais só com o contador. ;) \nPorém, não dá pra mostrar a posição. ')

print('\n*** Utilizando ENEMURATE:')
for pos, cont in enumerate(names):
    print(f'Nome: {cont}, na posição {pos}')

