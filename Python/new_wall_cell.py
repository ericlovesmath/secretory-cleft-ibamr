import os
from math import cos, hypot, pi, sin, sqrt

FOLDER_NAME = "fila_256"
try:
    os.mkdir(FOLDER_NAME)
except OSError:
    print(f"Directory {FOLDER_NAME} already exists")
else:
    print(f"Created directory {FOLDER_NAME}")


def b10(num):
    """Decimal to Scientific Notation"""
    return "{:.10e}".format(num)


def dist(p1, p2):
    return hypot(p2[0] - p1[0], p2[1] - p1[1])


class Circle:
    """Generates coordinates of circle"""

    def __init__(self, x, y, r, n):
        self.x = x
        self.y = y
        self.r = r
        self.n = n
        self.coords = [
            (
                cos(2 * pi / N_CELL * i) * r + x,
                sin(2 * pi / N_CELL * i) * r + y,
            )
            for i in range(0, N_CELL)
        ]
        self.vert_count = len(self.coords)
        self.spring_count = len(self.coords)
        self.beam_count = len(self.coords)

    def rotate(self, angle):
        self.coords = [
            (
                cos(2 * pi / N_CELL * i + angle) * r + x,
                sin(2 * pi / N_CELL * i + angle) * r + y,
            )
            for i in range(0, N_CELL)
        ]

    def gen_spring(self, offset=0):
        return [
            f"{(x)%self.vert_count + offset} {(x+1)%self.vert_count + offset} "
            f"{b10(SPRING_CONSTANT)} {b10(REST_LENGTH)}\n"
            for x in range(self.spring_count)
        ]

    def gen_beam(self, offset=0):
        return [
            f"{(x)%self.vert_count+offset} {(x+1)%self.vert_count+offset} "
            f"{(x+2)%self.vert_count+offset} "
            f"{b10(RIGIDITY)}\n"
            for x in range(self.vert_count)
        ]


class Wall:
    """Generates coordinates of a wall"""

    def __init__(self, x1, y1, x2, y2, n):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.n = n
        self.coords = [
            (x1 + i * (x2 - x1) / n, y1 + i * (y2 - y1) / n)
            for i in range(0, n + 1)
        ]
        self.vert_count = len(self.coords)
        self.spring_count = len(self.coords) - 1
        self.beam_count = len(self.coords) - 2

    def gen_spring(self, offset=0):
        return [
            f"{x+offset} {x+offset+1} {b10(SPRING_CONSTANT)} "
            f"{b10(dist(self.coords[x], self.coords[x+1]))}\n"
            for x in range(self.spring_count)
        ]

    def gen_beam(self, offset=0):
        return [
            f"{x+offset} {x+1+offset} {x+2+offset} " f"{b10(RIGIDITY)}\n"
            for x in range(self.beam_count)
        ]


# Variables
r, (x, y) = 2, (6, 4)  # Circle 1, Radius and Center
N_CELL = 32  # Number of Points
SPRING_CONSTANT = 200  # Spring Constant
REST_LENGTH = round(
    r * sqrt(2 - 2 * cos(2 * pi / N_CELL)), 3
)  # Rest Length (recommended listed)
RIGIDITY = 4000000  # Beam RIGIDITY

##########################################################################################
#################################### Vertex Formation ####################################
##########################################################################################

# x-coord, y-coord

file_out = open(f"./{FOLDER_NAME}/fila_256.vertex", "w")


target_cell = Circle(x, y, r, N_CELL)

verts = target_cell.vert_count
file_out.write(f"{verts}\n")

for point in target_cell.coords:
    file_out.write(f"{b10(point[0])} {b10(point[1])}\n")

print(f"Success: ~/{FOLDER_NAME}/fila_256.vertex")
file_out.close()

##########################################################################################
#################################### Spring Formation ####################################
##########################################################################################

# idx1, idx2, spring constant, rest length

file_out = open(f"./{FOLDER_NAME}/fila_256.spring", "w")

springs = target_cell.spring_count

file_out.write(f"{springs} # number of springs in file\n")

for spring in target_cell.gen_spring():
    file_out.write(spring)

file_out.close()

print(f"Success: ~/{FOLDER_NAME}/fila_256.spring")

##########################################################################################
##################################### Beam Formation #####################################
##########################################################################################

# idx1, idx2, idx3, rigidity
file_out = open(f"./{FOLDER_NAME}/fila_256.beam", "w")

file_out.write(
    f"{target_cell.beam_count}" "# INACCURATE number of beams in file\n"
)

for beam in target_cell.gen_beam():
    file_out.write(beam)

file_out.close()

print(f"Success: ~/{FOLDER_NAME}/fila_256.beam")
