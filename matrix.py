import math


def print_matrix( matrix ):
    if len(matrix) > 0:
        string = ""
        for row in range(len(matrix[0])):
            for col in range(len(matrix)):
                string += str(matrix[col][row]) + " "
            string = string[:len(string) - 1] #remove trailing " "
            string += "\n"
        string = string[:len(string) - 1] #remove trailing "\n"
        print string
            
#assume it's square?
def ident( matrix ):
    for col in range(len(matrix)):
        for row in range(len(matrix[0])):
            if col == row:
                matrix[col][row] = 1
            else:
                matrix[col][row] = 0
    return matrix

def scalar_mult( matrix, s ):
    for col in range(len(matrix)):
        for row in range(len(matrix[0])):
            matrix[col][row] *= s
    return matrix
            
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    ret = new_matrix( len(m2[0]), len(m2))
    return ret
    """
 for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            for (int k = 0; k < N; k++)
                    c[i][j] += a[i][k] * b[k][j];    

"""
    

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
