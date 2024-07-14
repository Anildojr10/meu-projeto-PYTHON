# Funções lambda (anônimas) - cria e usa na mesma hora
# Sintaxe:
# lambda argumentos: expressão

# Função lambda que retorne o quadrado de um número:
# quadrado = lambda x: x**2

# for i in range(1,11):
#     print(quadrado(i))

# Função para verificar se um número é par
# par = lambda x: x %2 == 0
# print(par(7))

# Função para converter grau Fahrenheit em Celsius
# f_c = lambda f: (f - 32) * 5/9
# print(f_c(32))

# Função map() - Permite usa uma outra função para cada elemento iterável (função que aplica funções)
# Sintaxe:
# map(função, iterável) ( Função de ordem superior)

# num = [1,2,3,4,5,6,7,8]
# dobro = list(map(lambda x: x * 2, num))
# print(dobro)

# palavras = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']
# maiusculas = list(map(str.upper, palavras))
# print(maiusculas)

# Função filter() : filtra elementos de uma sequência
# Sintaxe:
# filter(função, sequencia)

# def numeros_pares(n):
#     return n % 2 == 0

# numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# num_par = list(filter(numeros_pares, numeros))
# print(num_par)


# numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# num_impar = list(filter(lambda x: x %2 != 0, numeros))
# print(num_impar)


# Função reduce(): realiza operações comulativas em uma sequência de elementos - retorna apenas um valor
# Sintaxe:
# reduce(função, sequencia, valor_inicial)

from functools import reduce

# def mult(x, y):
#     return x * y

# numeros = [1,2,3,4,5,6]

# total = reduce(mult, numeros)  
# print(total)


# Soma cumulativa dos quadrados de valores, usando expressão lambda

numeros = [1,2,3,4] # ((1² + 2²)² + 3²)² + 4²

total = reduce(lambda x, y: x**2 + y**2, numeros)
print(total)

















