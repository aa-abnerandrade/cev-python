print('\033[1;7;30m AULA 17: LISTAS \033[m')

print('\n\033[1;7;40m PECULIARIDADES DAS LISTAS \033[m')
print('Quando fazemos uma lista receber outra, criamos uma LIGAÇÃO entre as duas.')
print('Esse comportamento é uma característica das LISTAS')

x = [2, 3, 4, 7]
y = x  # y recebe x ? não, ele faz uma ligação entre as listas
print(f" Lista X {x}")
print(f" Lista Y {y}")

print('\nSe eu alterar um elemento na lista Y... ')
y[2] = 3
print(f" Nova lista Y: {y}")
print(f"Consequentemente, \n Nova lista X: {x}")

print('\nPosso realizar uma cópia da lista assim: ')
y = x[:] # y recebe todos os itens de x
y[2] = 0
print(f" Outra versão de Y: {y}")
print(f" Mesma versão de X: {x}  * que na verdade, não mudou ")
