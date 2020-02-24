from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()


id = new_matrix()
id = ident(id)

x = 0
y = 0
for i in range(500):
    x1 = (x * 5)
    y1 = (y * 3 + 100)
    add_edge(matrix, x, y, 0, x + x1, y + y1, 0)
    x = (x + 10) % 500
    y = (y + 1) % 500

draw_lines( matrix, screen, color )
display(screen)
