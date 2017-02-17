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
            

def ident( matrix ):
    pass

def scalar_mult( matrix, s ):
    for row in range(len(matrix[0])):
        for col in range(len(matrix)):
            matrix[col][row] *= s
    return matrix
            
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    pass

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
