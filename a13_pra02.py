print('\033[7;40m AULA 13 - ESTRUTURA DE REPETIÇÃO FOR \033[m')

print('\n- Contagem personalizada')
number = int(input('Digite um número: '))
for c in range(0, number):
    print(c+1)

print()

print('- Nova contagem personalizada ')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)