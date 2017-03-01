from display import *
from draw import *
import random

screen = new_screen()
color = [ random.randint(0, 255), random.randint(0, 255), random.randint(0, 255) ]
matrix = []

print "adding points (0, 0, 0) (50, 50, 0) (100, 0, 0) (50, 100, 0)"
add_point(matrix, 0, 0, 0)
add_point(matrix, 50, 50, 0)
add_point(matrix, 100, 0, 0)
add_point(matrix, 50, 100, 0)

print_matrix(matrix)
print ""

print "adding edge (50, 100, 0) (200, 100, 0)"
add_edge(matrix, 50, 100, 0, 200, 100, 0)

print_matrix(matrix)
print ""

print "identity matrix"
identity = new_matrix()
ident(identity)

print_matrix(identity)
print ""

print "scale identity matrix"
scalar_mult(identity, 2)

print_matrix(identity)
print ""

print "matrix mult: scaled identity * matrix"
matrix_mult(identity, matrix)
print_matrix(matrix)
print ""

#===================================================

matrix = []
n = random.randint(5, 20)
for i in range(n):
    add_point(matrix, random.randint(0, 50), random.randint(0, 50))
for trials in range(5):
    color = [ random.randint(0, 255), random.randint(0, 255), random.randint(0, 255) ]
    draw_lines( matrix, screen, color )
    scalar_mult(matrix, 2)

display(screen)
