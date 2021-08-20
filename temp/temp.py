import os
from math import cos, pi,  sqrt
import cellObjects as obj

FOLDER_NAME = "fila_256"

try:
    os.mkdir(FOLDER_NAME)
except OSError:
    print(f"Directory {FOLDER_NAME} already exists")
else:
    print(f"Created directory {FOLDER_NAME}")

def b10(num):
    """Decimal to Scientific Notation."""
    return "{:.10e}".format(num)

# Variables
r, (x, y) = 2, (6, 4) # Circle 1, Radius and Center
x1, y1, x2, y2 = 2, 1, 2, 7
N_CELL = 32  # Number of Points
N_WALL = 32  # Number of Points
SPRING_CONSTANT = 200  # Spring Constant

# Rest Length (recommended listed)
REST_LENGTH = round(r * sqrt(2 - 2 * cos(2 * pi / N_CELL)), 3)
RIGIDITY = 4000000  # Beam RIGIDITY

###############################################################################
#                             Object Formation                                #
###############################################################################

cell_wall = obj.Wall(x1, y1, x2, y2, N_WALL, SPRING_CONSTANT, RIGIDITY)
target_cell = obj.Circle(x, y, r, N_CELL, SPRING_CONSTANT, REST_LENGTH, RIGIDITY)

###############################################################################
#                             Vertex Formation                                #
###############################################################################

# x-coord, y-coord

file_out = open(f"./{FOLDER_NAME}/fila_256.vertex", "w")

verts = cell_wall.vert_count + target_cell.vert_count

file_out.write(f"{verts}\n")

for point in cell_wall.coords + target_cell.coords:
    file_out.write(f"{b10(point[0])} {b10(point[1])}\n")

print(f"Success: ~/{FOLDER_NAME}/fila_256.vertex")
file_out.close()

###############################################################################
#                               Spring Formation                              #
###############################################################################

# idx1, idx2, spring constant, rest length

file_out = open(f"./{FOLDER_NAME}/fila_256.spring", "w")

springs = cell_wall.spring_count + target_cell.spring_count

file_out.write(f"{springs} # number of springs in file\n")

for spring in cell_wall.gen_spring():
    file_out.write(spring)

for spring in target_cell.gen_spring(cell_wall.vert_count):
    file_out.write(spring)

file_out.close()

print(f"Success: ~/{FOLDER_NAME}/fila_256.spring")

###############################################################################
#                               Beam Formation                                #
###############################################################################

# idx1, idx2, idx3, rigidity
file_out = open(f"./{FOLDER_NAME}/fila_256.beam", "w")

file_out.write(
    f"{cell_wall.beam_count + target_cell.beam_count}"
    "# INACCURATE number of beams in file\n"
)

for beam in cell_wall.gen_beam():
    file_out.write(beam)

for beam in target_cell.gen_beam(cell_wall.vert_count):
    file_out.write(beam)

file_out.close()

print(f"Success: ~/{FOLDER_NAME}/fila_256.beam")
