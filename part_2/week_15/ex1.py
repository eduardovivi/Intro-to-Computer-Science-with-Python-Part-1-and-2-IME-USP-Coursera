def  soma_lista(lista):
    ''' recebe como parâmetro uma lista de números inteiros e devolve um número inteiro correspondente à soma dos elementos desta lista com uso de recursao'''
    if (len(lista) == 1):
        return lista[0]
    else:
        a = lista[1:]
        valor = lista[0] + soma_lista(a)
    
    return valor
