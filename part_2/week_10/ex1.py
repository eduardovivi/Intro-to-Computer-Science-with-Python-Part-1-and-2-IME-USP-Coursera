
def calcula_dimensoes(matrix):
    height = len(matrix)
    width = 1
    for item in matrix:
        width = len(item)
        break
    return "{}".format(height) + "X" + "{}".format(width)

def dimensoes(matrix):
    print(calcula_dimensoes(matrix))

minha_matriz = [[1], [2], [3]]
dimensoes(minha_matriz)