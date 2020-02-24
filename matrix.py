"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    for point in matrix:
        line1 += (str(point[0]) + " ")
        line2 += (str(point[1]) + " ")
        line3 += (str(point[2]) + " ")
        line4 += (str(point[3]) + " ")
    print(line1)
    print(line2)
    print(line3)
    print(line4)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for x in range(len(matrix)):
        for y in range(4):
            if x == y:
                matrix[x][y] = 1
            else:
                matrix[x][y] = 0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m3 = new_matrix()
    for x in range(len(m2)):
        temp = list(m2[x])
        for y in range(len(m1[0])): #range(4) really
            sum = 0
            for i in range(len(m1)):
                sum += m1[i][y] * m2[x][i]
            m3[x][y] = sum
            temp[y] = sum
        m2[x] = temp
    return m2




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

'''
id = new_matrix()
print_matrix(id)
print()
ident(id)
print_matrix(id)
print()
a = [[3, 4, 2, 1], [4, 3, 6, 1], [2, 3, 4, 1], [6, 8, 9, 1]]
print_matrix(a)

matrix_mult(id, a)
print()
print_matrix(a)
'''
