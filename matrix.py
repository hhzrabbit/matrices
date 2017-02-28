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

def scalar_mult( matrix, s ):
    for col in range(len(matrix)):
        for row in range(len(matrix[0])):
            matrix[col][row] *= s
            
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    temp = new_matrix( len(m2[0]), len(m2))
    
    for i in range(len(m1)):
        for j in range(len(m2)):
            for k in range(len(m2[0])):
                 temp[j][i] += m1[k][i] * m2[j][k]

    for col in range(len(temp)):
        for row in range(len(temp[0])):
            m2[col][row] = temp[col][row]

    

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
