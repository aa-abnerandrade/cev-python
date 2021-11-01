print('='*5, ' QUADRO DE OPERAÇÕES ', '='*5)
print ('Seja bem vindo! ')
name = str(input('Por favor, digite seu nome: '))
n1 = int(input('{}, por favor digite um número: ' .format(name)))
n2 = int(input('Agora digite outro número: '))
print()
soma = n1 + n2
mult = n1 * n2
div = n1 / n2
di = n1//n2
exp = n1 ** n2
print('===== RESULTADOS: ')
print('A soma é {}, o produto é {} e a divisão é {:.2f}. ' .format(soma, mult, div), end=' ')
print('A divisão inteira é {} e a potência é {}. ' .format(di, exp))
