print('\033[1;7;40m AULA 17: LISTAS \033[m')

# com RANGE
print('\n com RANGE: ')
valores = list(range(4, 10+1))
print(valores)

# ou posso declarar os valores
print('\n com declaração: ')
valores = [8, 2, 5, 4, 9, 3, 0]
print(valores)

# e com SORT posso organizar os valores na própria lista
print('\n organizar os valores com SORT: ')
valores.sort()
print(valores)
# organizando em ordem reversa
print(' ou até mesmo organizar em ordem reversa: ')
valores.sort(reverse=True)
print(valores)

# podemos também utilizar o LEN
valores = [8, 2, 5, 4, 9, 3, 0]
print(f"\n Aqui o LEN também vale: {len(valores)}")