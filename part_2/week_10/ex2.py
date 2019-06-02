
def calcula_dimensoes(matrix):
    height = len(matrix)
    width = 1
    for item in matrix:
        width = len(item)
        break
    return height, width

def soma_matrizes(m1, m2):
    h, w = calcula_dimensoes(m1)
    if calcula_dimensoes(m1) != calcula_dimensoes(m2):
        return False
    else:
        m3 = m1
        for i in range(0,h):
            for j in range(0,w):
                m3[i][j] = m1[i][j] + m2[i][j]
    return m3