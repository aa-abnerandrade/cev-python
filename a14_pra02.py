print('\033[7;40m AULA 13 - ESTRUTURA DE REPETIÇÃO WHILE \033[m')

print('VERIFICADOR DE PAR OU ÍMPAR')
print('Insira 0 para sair.\n')
answer = 1
tot = totpar = totimp = 0

while answer != 0:
    answer = int(input('Informe um valor: '))
    if answer != 0:
        if (answer % 2 == 0):
            totpar += 1
        else:
            totimp += 1
        tot += 1

print(f'\nDos {tot} valores digitados, {totpar} são pares e {totimp} são ímpares. ')