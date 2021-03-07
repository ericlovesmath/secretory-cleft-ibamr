# Reading File
from math import cos, sin, pi, sqrt

Big_Cell = []
Small_Cell = []
for i, line in enumerate(open(f"./VisExport/Analysis/{format(4, '04')}.txt", "r")):
    values = [float(s) for s in line.split()]
    print(f"({values[0]}, {values[1]})")
    if i < 80:
        Big_Cell.append(values)
    else:
        Small_Cell.append(values)
        
print(Big_Cell)
print(Small_Cell)

def b10(num):
    return "{:.10e}".format(num)
def circ(x, y, r, n):                            # Generates Circle coordinates
    return [(cos(2*pi/n*i)*r + x, sin(2*pi/n*i)*r + y)
        for i in range(0,n)]

folder_name = "fila_256"
file_out = open(f"./Python/{folder_name}/fila_256.vertex", "w")
file_out.write("144 # INACCURATE number of vertices in file\n")

#####
#cleft = circ(Big_Cell[0][0],Big_Cell[0][1],0.5,16)
#cleft = cleft[4:13]
#Cleft_Big_Cell = Big_Cell[2:78] + cleft
n = 64
dx = Big_Cell[n//16 + 1][0] - Big_Cell[0][0]
dy = Big_Cell[n//16 + 1][1] - Big_Cell[0][1]
rad = sqrt(dx**2 + dy**2)
print(rad)
mini_circ = circ(Big_Cell[0][0], Big_Cell[0][1], rad/2, n//4)

for x in range(-1*n//16 ,n//16 + 1):
    Big_Cell[x] = mini_circ[n//8-x]
#####

for point in Big_Cell + Small_Cell:
    file_out.write(f"{b10(point[0])} {b10(point[1])}\n")


file_out.write("# x-coord, y-coord\n")
file_out.close()

#################################33 Spring
# Variables
r1, (x1, y1) = 1, (2, 3)                       # Circle 1, Radius and Center
r2, (x2, y2) = 1, (5, 3)                         # Circle 2, Radius and Center
n = 64                                           # Number of Points
spring_const = 50                              # Spring Constant
rest_length = round(r1*sqrt(2-2*cos(2*pi/n)), 3) # Rest Length (recommended listed)
Rigidity = 4000000                               # Beam Rigidity
r_sm = r1*(0.4)                                  # Radius of Smaller Circles
n_sm = n//2                                      # Number of Points on Smaller Circles
# Generates small circles centered at pi/4 and -pi/4 radians
sm_center = n//8                                 # Center Angle (pi/8 radians)
sm_start = n_sm//8                               # Small Circle offset Left/Right
sm_half = n_sm//2                                # Small Circle Arc length
circ_sm_rad = n//16                              # Large Circle removing arc radius


file_out = open(f"./Python/{folder_name}/fila_256.spring", "w")

file_out.write(f"{n + n + sm_center + 1} # INACCURATE number of springs in file\n")

Cells = Big_Cell + Small_Cell
for i in range(len(Big_Cell)):
    cur_len = sqrt((Big_Cell[i][0] - Big_Cell[(i+1)%len(Big_Cell)][0])**2 + (Big_Cell[i][1] - Big_Cell[(i+1)%len(Big_Cell)][1])**2)
    file_out.write(f"{i%len(Big_Cell)} {(i+1)%len(Big_Cell)} {b10(spring_const)} {b10(cur_len)}\n")

for i in range(len(Small_Cell)):
    cur_len = sqrt((Small_Cell[i][0] - Small_Cell[(i+1)%len(Small_Cell)][0])**2 + (Small_Cell[i][1] - Small_Cell[(i+1)%len(Small_Cell)][1])**2)
    file_out.write(f"{80 + i%len(Small_Cell)} {80 + (i+1)%len(Small_Cell)} {b10(spring_const)} {b10(cur_len)}\n")

###### PULL BARS #####
##for x in range(-1*n//16, n//16 + 1):
#    pb_len = sqrt((Big_Cell[n//2 - 3*x][0]-Big_Cell[x%n][0])**2 + (Big_Cell[n//2 - 3*x][1]-Big_Cell[x%n][1])**2)
#    file_out.write(f"{n//2 - 3*x} {x%n} {b10(spring_const//10)} {b10(pb_len)}\n")

###  CONNECTING BARS ###

#for x in range(1,5*n_sm//16):
#    file_out.write(f"{n//16 + x} {n + n//2 - n//4 - x} {b10(spring_const)} {b10(0.2)}\n")
#for x in range(1,5*n_sm//16):
#    file_out.write(f"{(-n//16 - x)%n} {n + n//2 + n//4 + x} {b10(spring_const)} {b10(0.2)}\n")

print(f"Success: ~/{folder_name}/fila_256.spring")

# https://sci-hub.se/https://academic.oup.com/imammb/article-abstract/30/2/115/890410?redirectedFrom=fulltext
# https://sci-hub.se/https://www.sciencedirect.com/science/article/pii/S0006349516000564