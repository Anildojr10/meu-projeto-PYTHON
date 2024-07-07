# Set: coleções não ordenadas de valores únicos

planeta_anao = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
print(len(planeta_anao))
# print('Ceres' in planeta_anao)

# for astro in planeta_anao:
#     print(astro.upper())

# astros = ['Lua', 'Vênus', 'Sirius', 'Marte', 'Lua']
# print(astros, end=' ')
# astro_set = set(astros)
# print(astro_set)

astros1 = {'Lua', 'Sirius', 'Marte', 'Vênus', 'Io'}
astros2 = {'Lua', 'Sirius', 'Marte', 'Vênus', 'Cometa Halley'}
# print(astros1 != astros2)
# print(astros1.union(astros2))

# print(astros1 & astros2)
# print(astros1.intersection(astros2))

# print(astros1 ^ astros2)
# print(astros1.symmetric_difference(astros2))

astros1.add('Urano')
astros1.add('Sol')
astros1.remove('Plutão')
astros1.pop()
print(astros1)