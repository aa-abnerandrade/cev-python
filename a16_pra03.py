print('\033[1;7;40m AULA 16: TUPLAS \033[m\n')

print('Mudando de contexto: ')
print('\nCONCATENAÇÃO DE TUPLAS: ')
a = (1, 8, 5, 10)
b = (21, 10, 13, 93, 70)
c = a + b
print('Sim, aqui a ordem altera o resultado final: ')
print(a+b)
print(b+a)
print(f'Colocando em ordem com SORTED: {sorted(c)}')

print('\nALGUMAS FUNÇÕES')
print(c)
print(f'Contando ocorrências: {c.count(10)}')
print(f'Encontrando a ocorrência 10 e revelando sua posição: {c.index(10)}') # Aqui se limita à primeira ocorrência
print(f'Podemos varrer indicando a partir de qual posição deve ser realizada a leitura: {c.index(10, 4)}') # deslocamento
