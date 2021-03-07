from math import cos, sin, pi, sqrt
import os

folder_name = "fila_256"
try: 
    os.mkdir(folder_name)
except OSError:
    print(f"Directory {folder_name} already exists")
else:
    print(f"Created directory {folder_name}")

# Decimal to Scientific Notation
def b10(num):                                    
    return "{:.10e}".format(num)

# Generates coordinates of circle
class Circle:
    def __init__(self, x, y, r, n):
        self.x = x
        self.y = y
        self.r = r
        self.n = n
        self.coords = [(cos(2*pi/n_circ*i)*r + x, sin(2*pi/n_circ*i)*r + y)
            for i in range(0,n_circ)]
    def rotate(self, angle):
        self.coords = [(cos(2*pi/n_circ*i + angle)*r + x, sin(2*pi/n_circ*i+ angle)*r + y)
            for i in range(0,n_circ)]

# Generates coordinates of a wall
class Wall:
    def __init__(self, x1, y1, x2, y2, n):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.n = n
        self.coords = [(x1 + i*(x2-x1)/n, y1 + i*(y2-y1)/n) 
            for i in range(0,n+1)]
        
# Variables
r, (x, y) = 2, (6, 4)                       # Circle 1, Radius and Center
x1, y1, x2, y2 = 2,1, 2,7
n_circ = 64                                           # Number of Points
n_wall = 64                                           # Number of Points
spring_const = 5000                              # Spring Constant
rest_length = round(r*sqrt(2-2*cos(2*pi/n_circ)), 3)  # Rest Length (recommended listed)
Rigidity = 4000000                               # Beam Rigidity

##########################################################################################
#################################### Vertex Formation ####################################
##########################################################################################

file_out = open(f"./{folder_name}/fila_256.vertex", "w")

cell_wall = Wall(x1, y1, x2, y2, n_wall).coords

target_cell = Circle(x,y,r,n_circ).coords

file_out.write(f"{n_wall + n_circ + 1}\n")
for point in cell_wall + target_cell:
    file_out.write(f"{b10(point[0])} {b10(point[1])}\n")

file_out.write("# x-coord, y-coord\n")

print(f"Success: ~/{folder_name}/fila_256.vertex")
file_out.close()

##########################################################################################
#################################### Spring Formation ####################################
##########################################################################################

file_out = open(f"./{folder_name}/fila_256.spring", "w")

file_out.write(f"{n_circ + n_wall} # INACCURATE number of springs in file\n")

for x in range(n_wall):
    file_out.write(f"{x} {x+1} {b10(spring_const)} {b10((y2-y1)/n_wall)}\n") #This will bite me later

for x in range(n_circ):
    file_out.write(f"{n_wall+1 + (x%n_circ)} {n_wall+1 + (x+1)%n_circ} {b10(spring_const)} {b10(rest_length)}\n")

file_out.write("# idx1, idx2, spring constant, rest length\n")
file_out.close()

print(f"Success: ~/{folder_name}/fila_256.spring")

##########################################################################################
##################################### Beam Formation #####################################
##########################################################################################

file_out = open(f"./{folder_name}/fila_256.beam", "w")

file_out.write(f"{128} # INACCURATE number of beams in file\n")

for x in range(n_wall+n_circ+1):
    file_out.write(f"{x%(n_wall+n_circ+1)} {(x+1)%(n_wall+n_circ+1)} {(x+2)%(n_wall+n_circ+1)} {b10(Rigidity)}\n")

file_out.write("# idx1, idx2, idx3, rigidity\n")
file_out.close()

print(f"Success: ~/{folder_name}/fila_256.beam")