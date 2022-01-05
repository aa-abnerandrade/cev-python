print('\033[1;7;40m AULA 17: LISTAS I \033[m\n')


print('*** EM LISTAS UTILIZAMOS COLCHETES [ ] : ')
lanche = ['Hamburguer', 'Refrigerante', 'Pizza', 'Picolé']
print(lanche)
lanche[1] = 'Suco'
print(lanche)
print()


print('\n\033[1;7;40m ALGUNS MÉTODOS DE LISTAS \033[m')

print('*** Inserindo um item: ') # Inserindo um item:
lanche.append('Cookie')
print(lanche)

print('\n*** Podemos inserir um item escolhendo uma posição: ') # Podemos inserir um item escolhendo uma posição:
lanche.insert(0, 'Hot Dog')
print(lanche)
lanche.insert(3, 'Milk Shake')
print(lanche)

print('\n*** Temos métodos para deletar: ') # Temos métodos para deletar:
# Os métodos DEL e POP servem pra remover um item conforme sua posição
del lanche[3]
print(lanche)
lanche.pop(3)
print(lanche)
print('> O método POP costuma ser usado para excluir o último elemento da lista: ')
lanche.pop()
print(lanche)
print('\n*** O método REMOVE faz a exclusão conforme o conteúdo: ') # O REMOVE exclui conforme o conteúdo
lanche.remove('Hot Dog')
print(lanche)

print('> Podemos usar REMOVE dentro de um condicional para evitar erros: ') # Usar IF para evitar erros
if 'Pizza' in lanche:
    lanche.remove('Pizza')
else:
    print(lanche)
