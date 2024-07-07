# Escopo Global e Local

var_global = "Curso Completo de Python"

def escrever_texto():
    global var_global
    var_global = "Bancos de Dados com SQL"
    var_local = "Anildo Jerônimo Silva Junior"
    print(f'Varival Global: {var_global}')
    print(f'Varival Local: {var_local}')

if __name__ == '__main__':
    print(f'Executar a função escrever_texto()')
    escrever_texto()

    print('Tentar acessar as variáveis diretamente')
    print(f'Varival Global: {var_global}')
    


