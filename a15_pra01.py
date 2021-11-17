print('\033[7;40m AULA 15 - INTERROMPENDO WHILE \033[m')
print()

cont = 1
while cont <= 10:
    print(cont, end=' → ')
    cont += 1
print('Fim')

cont = 1
while True:
    print(cont, end=' → ')
    cont += 1
    if cont == 10+1:
        break
print('Fim')

print('\n\033[1mOutro exemplo: \033[m')
number = soma = 0
while True:
    number = int(input('Qual valor deseja somar? '))
    if number == 0:
        break
    soma += number
print(f'Resultado: {soma}')
