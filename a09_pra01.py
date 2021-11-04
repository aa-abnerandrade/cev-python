print('AULA 08 - MANIPULANDO TEXTO')

print()
frase = 'Curso em Vídeo Python'
print(frase)

# Fatiamento - maior uso de colchetes []
print('\nFATIAMENTO')
print(f'O caractere que ocupa o 9° espaço na sentença é {frase[9]}.')
print(f'Do 9° ao 13° caractere obtemos: {frase[9:14]}')  # O último valor não entra na contagem
print(f'Do 9º ao 21° pulando de 2 em 2, teremos: {frase[9:21:2]}')
print(f'Até o caractere no espaço 4: {frase[0:5]}')  # O 0 (zero) pode ser omitido, ficaria frase[:5]
print(f'Do 15° caractere em diante, ficaria: {frase[15:]}')
print(f'Do 9° caractere até o final, pulando de 3 em 3, retorna: {frase[9::3]}')

# Análise - uso predominante de parênteses ()
print('\nANÁLISE')
print(f'Quantidade de espaços que a string ocupa: {len(frase)}')
print('Quantas vezes aparece a letra "o" (minúsculo): {}'.format(frase.count('o')))
print('Da posição 0 até o 12, quantas vezes aparece a letra o (minúsculo): {} '.format(frase.count('o', 0, 13)))  # Colocamos 13 e o sistema contará até 12
print('Resultado retornado para o parâmetro dado: {}'.format(frase.find('deo')))  # Em que espaço começa a sentença 'deo'
print('Quando o termo de buscado não for localizado na string em questão: {}'.format(frase.find('Android')))  # O sistema retorna -1 (menos um)
print('Contém o termo "Curso" na frase: {}'.format('Curso' in frase))

# Transformação
print('\nTRANSFORMAÇÃO')
print('Substituição de termo: {}'.format(frase.replace('Python', 'Cobra')))
print(f'Em maiúscula: {frase.upper()}')
print(f'Em minúsculo: {frase.lower()}')
print(f'Apenas a primeira da frase em maíusculo (capitalizada): {frase.capitalize()}')
print(f'Cada palavra em maiúscula: {frase.title()}')
print(f'Retirar espaços inúteis no início e fim da sentença: {frase.strip()}')
print(f'Retirar espaços inúteis apenas no fim da sentença: {frase.rstrip()}')
print(f'Retirar espaços inúteis apenas no início da sentença: {frase.lstrip()}')

# Divisão
print('\nDIVISÃO')
print(f'A função SPLIT cria uma lista, por intermédio dos espaços na sentença: {frase.split()}')  # É possível informar parâmetros nos parênteses do spli
print('A função JOIN junta uma lista, separando os termos pelo caractere informado como parâmetro {} '.format('-'.join(frase)))

# Outros
print('\nOUTROS')
print('Colocamos tudo em maiúsculo e pedimos pra contar "O": {} vezes ' .format(frase.upper().count('O')))  # utilizando dois métodos conjuntamente
print(frase.join(frase.split()))
dividido = frase.split()
print('Aqui, dividimos a string - {} - e pedimos que imprima apenas o trecho da posição 0 (zero) - {} - .'.format(dividido, dividido[0]))
print(
    'Aqui, dividimos a string - {} - e pedimos que imprima: o espaço 3 (três) do trecho da posição 0 (zero) - {} - .'.format(dividido, dividido[0][3]))
