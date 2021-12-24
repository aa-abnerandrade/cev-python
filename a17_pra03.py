print('\033[1;7;30m AULA 17: LISTAS \033[m')

print('\n\033[1;7;40m DECLARANDO LISTAS \033[m')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

print('Valores: ', end='')
for v in valores:
    print(f" {v}... ", end='')
print()

print('\nOu então, podemos perguntar ao usuário: ') # com RANGE:

valores = []
for c in range(0, 4+1):
    valores.append(int(input('Digite um valor: ')))
print(f" Os valores digitados foram: {valores} ")

print('\n\033[1;7;40m EXIBINDO LISTAS \033[m') # exibindo listas

print()
for c, v in enumerate(valores):
    print(f"Valor: {v} | Posição: {c}")
print('Lista finalizada!'.center(21))



