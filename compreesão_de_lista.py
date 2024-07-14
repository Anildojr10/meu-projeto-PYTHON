# Algoritmo para encontrar os quadrados de números de uma lista ( sem compreesão de lista)
# numeros = [1,4,7,9,10,11,21]

# quadrados = list(map(lambda num: num**2, numeros))
# print(quadrados)


# Com compreensão de lista
# numeros = [1,4,7,9,10,11,21]

# quadrados = [num**2 for num in numeros]
# print(quadrados)

# Criar um lista de números pares de 1 a 10
# pares = [num for num in range(21) if num % 2 == 0]
# print(pares)


# Contar a quantidade de vogais dentro de um texto
# frase = 'A lógica é apenas o princípio da sabedoria, e não o seu fim.'
# vogais = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']

# lista_vogais = [v for v in frase if v in vogais]
# print(f' A frase possui {len(lista_vogais)} vogais:')
# print(lista_vogais)


# Fazer uma operação disributiva entre números de duas listas
distributiva = [k * m for k in [2,3,5] for m in [10,20,30]]
print(distributiva)







