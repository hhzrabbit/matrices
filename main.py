from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = []


print "adding points (0, 0, 0) (100, 100, 0) (200, 0, 0) (100, 200, 0)"
add_point(matrix, 0, 0, 0)
add_point(matrix, 100, 100, 0)
add_point(matrix, 200, 0, 0)
add_point(matrix, 100, 200, 0)

print_matrix(matrix)



print "adding edge (100, 200, 0) (400, 200, 0)"
add_edge(matrix, 100, 200, 0, 400, 200, 0)





print "identity matrix"
identity = new_matrix()
ident(identity)
print_matrix(identity)

print ""

print "scale identity matrix"
scalar_mult(identity, 2)
print_matrix(identity)

print ""

print "matrix matrix mult"
matrix_mult(identity, matrix)
#print_matrix(ret)
print_matrix(matrix)


draw_lines( matrix, screen, color )
#display(screen)
