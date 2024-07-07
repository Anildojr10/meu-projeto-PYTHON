# Funções
# Modularização, Reuso de código, Legibilidade 

# Sintaxe:
# def <nome_função> ([argumentos]):
#     <instruções>    

# def mensagem():
#     print('Bóson Treinamentos em Tecnologi')
#     print('Curso Completo de Python.')

# mensagem()

# Função com arugmentos
# def soma(a, b):
#     print(a+b)

# soma(12, 7)

# def mult(x, y):
#     return x * y

# a = 5
# b = 8
# c = mult(a, b)
# print(f'o produto de {a} e {b} é {c}')

# def div(k, j):
#     if j != 0:
#         return k / j
#     else:
#         return 'Imporssível dividir por zero!'

# if __name__ == '__main__':
#     a = int(input('Digite um númer: '))
#     b = int(input('Digite outro número: '))
    
#     r = div(a, b)
#     print(f'{a} dividido por {b} é igual a {r}')


# def quadrado(val):
#     quadrados = []
#     for x in val:
#         quadrados.append(x ** 2)
#     return quadrados

# if __name__ == '__main__':
#     valores = [2,5,7,9,12]
#     resultados = quadrado(valores)
#     for g in resultados:
#         print(g)

# def contar(num=11, caractere='+'):
#     for i in range(1, num):
#         print(caractere)

x = 5
y = 6
z = 3

def soma_mult(a, b, c = 0):
    if c == 0:
        return a * b
    else:
        return a + b + c
    
if __name__ == '__main__':
    res = soma_mult(x, y, z)
    print(res)
