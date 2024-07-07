# Dicionários perminitem armazenar dados em pares chaves/valor

elemento = {'Z': 3, 
            'nome': 'Lítio', 
            'grupo': 'Metais Alcalinos', 
            'densidade': 0.534
}

print(f'Elemento: {elemento['nome']}')
print(f'Densidade: {elemento['densidade']}')
print(f'O Dicionário possui {len(elemento)} elementos. ')

# Atualizar uma entrada 
elemento['grupo'] = 'Alcalinos'
print(elemento)

# Adicionar uma entrada
elemento['periodo']= 1
print(elemento)

# # Exclusão de itens em dicionário
# del elemento['periodo']
# print(elemento)

# # Apagar os elementos de um dicionário
# elemento.clear()

# # Apagar um dicionário
# del elemento

print(elemento.items())
for i in elemento.items():
    print(i)

print(elemento.keys())
for i in elemento.keys():
    print(i)

print(elemento.values())
for i in elemento.values():
    print(i)

for i, j in elemento.items():
    print(f'{i}: {j}')