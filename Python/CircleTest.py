from math import cos, sin, pi, sqrt
import os

folder_name = "fila_256"
try: 
    os.mkdir(folder_name)
except OSError:
    print(f"Directory {folder_name} already exists")
else:
    print(f"Created directory {folder_name}")

def b10(num):                                    # Decimal to Scientific Notation
    return "{:.10e}".format(num)

def circ(x, y, r, n):                            # Generates Circle coordinates
    return [(cos(2*pi/n*i)*r + x, sin(2*pi/n*i)*r + y)
        for i in range(0,n)]

# Variables
r1, (x1, y1) = 1, (2.5, 2)                       # Circle 1, Radius and Center
r2, (x2, y2) = 1, (5, 2)                         # Circle 2, Radius and Center
n = 64                                           # Number of Points
spring_const = 5000                              # Spring Constant
rest_length = round(r1*sqrt(2-2*cos(2*pi/n)), 3) # Rest Length (recommended above)
Rigidity = 5000000                               # Beam Rigidity
r_sm = r1*(0.4)                                  # Radius of Smaller Circles
n_sm = n//2                                      # Number of Points on Smaller Circles
# Generates small circles centered at pi/4 and -pi/4 radians
sm_center = n//8                                 # Center Angle (pi/8 radians)
sm_start = n_sm//8                               # Small Circle offset Left/Right
sm_half = n_sm//2                                # Small Circle Arc length
circ_sm_rad = n//16                              # Large Circle removing arc radius

##########################################################################################
#################################### Vertex Formation ####################################
##########################################################################################

file_out = open(f"./{folder_name}/fila_256.vertex", "w")

# 2 Circles, rough outline of cells
circ_1 = circ(x1,y1,r1,n)
circ_2 = circ(x2,y2,r2,n)

####### SMALL CIRCLE 1 ######

# Generates small circles centered at pi/4 and -pi/4 radians
sm_circ_1 = circ(circ_1[sm_center][0],     circ_1[sm_center][1],     r_sm, n_sm)
sm_circ_2 = circ(circ_1[n - sm_center][0], circ_1[n - sm_center][1], r_sm, n_sm)

# Cuts small circles inside larger circle
sm_circ_1 = sm_circ_1[n_sm - sm_start:]    + sm_circ_1[:sm_half  - sm_start + 1]
sm_circ_2 = sm_circ_2[sm_half + sm_start:] + sm_circ_2[:sm_start + 1]

# Replace overlap with cut small circle
circ_1[n - sm_center - circ_sm_rad : n - circ_sm_rad + 1] = sm_circ_2
circ_1[circ_sm_rad : sm_center + circ_sm_rad + 1] = sm_circ_1

n_big = len(circ_1)

# File output
file_out.write(f"{n_big + n} # number of vertices in file\n")

for point in circ_1 + circ_2:
    file_out.write(f"{b10(point[0])} {b10(point[1])}\n")

file_out.write("# x-coord, y-coord\n")

print(f"Success: ~/{folder_name}/fila_256.vertex")
file_out.close()

##########################################################################################
#################################### Spring Formation ####################################
##########################################################################################

file_out = open(f"./{folder_name}/fila_256.spring", "w")

file_out.write(f"{n_big + n + sm_center + 1} # INACCURATE number of springs in file\n")

for x in range(n_big):
    file_out.write(f"{x%n_big} {(x+1)%n_big} {b10(spring_const)} {b10(rest_length)}\n")

for x in range(n):
    file_out.write(f"{n_big + (x%n)} {n_big + (x+1)%n} {b10(spring_const)} {b10(rest_length)}\n")

######  PULL BARS #####
#for x in range(-1*n//16 ,n//16 + 1):
#    pullbar_len_formula = 0.5 - 0.02*abs(x) # <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- 
#    print(pullbar_len_formula)
#    file_out.write(f"{n_big//2 - 4*x} {x%n_big} {b10(spring_const)} {b10(pullbar_len_formula)}\n")

###  CONNECTING BARS ###

#for x in range(1,5*n_sm//16):
#    file_out.write(f"{n//16 + x} {n_big + n//2 - x - n//9} {b10(spring_const)} {b10(0.1)}\n")
#for x in range(1,5*n_sm//16):
#    file_out.write(f"{(-n//16 - x)%n_big} {n_big + n//2 + x + n//9} {b10(spring_const)} {b10(0.1)}\n")

file_out.write("# idx1, idx2, spring constant, rest length\n")
file_out.close()

print(f"Success: ~/{folder_name}/fila_256.spring")

##########################################################################################
##################################### Beam Formation #####################################
##########################################################################################

file_out = open(f"./{folder_name}/fila_256.beam", "w")

file_out.write(f"{7*n_big//8+n-1} # INACCURATE number of beams in file\n")

for x in range(n_big):
    file_out.write(f"{x%n_big} {(x+1)%n_big} {(x+2)%n_big} {b10(Rigidity)}\n")
# \/ is for the beamless center
#for x in range(n_big//16 + 1, 15*n_big//16):
#    file_out.write(f"{x%n_big} {(x+1)%n_big} {(x+2)%n_big} {b10(Rigidity)}\n")
for x in range(n):
    file_out.write(f"{n_big+x%n} {n_big+(x+1)%n} {n_big+(x+2)%n} {b10(Rigidity*100)}\n")

file_out.write("# idx1, idx2, idx3, rigidity\n")
file_out.close()

print(f"Success: ~/{folder_name}/fila_256.beam")

##################################################################################
#  More vertices            --->    Doesn't help until 64, stops moving at 128   #
#  Spring2d Input2D         --->    ... I forgot what I meant by this            #
#  Changing Spring Constant --->    Doesn't change much                          #
#  Changing Beam Constant   --->    Check                                        #
#  Lower CFL or Timestep    --->    Takes longer, doesn't do anything important  #
#  Extending Spring Lengths --->    Deforms cells by making them fluff or crush  #
#                                                                                #
#  Docker Container working in local server                                      #
#  Alternate Springs code lost on Palmtree restart(?)                            #
#        Backup to GitHub or local server                                        #
#                                                                                #
#  Goals                                                                         #
#    - Fix ordering of sm circle vertices                                     #
#    - Scale cleft springsw                                                      #
#    - Envelopment                                                               #
##################################################################################
# Removing intial self intersections
# Spread out internal connections
# Remove beams on inside of cleft
#   Testing out beams
# Stability

# . mass file (mass to points)
# Add springs to inside so it doesn't just collapse on the other one
    # Massive spring constant

# markdown tutorial
# Docker cp
# Add them as collab 
# Add docker link somehow???
# Make the markdown file like a tutorial
# Make movie recordings
# Organize simulation files 

# Think about 3d?
# Self intersection and permeability
# Correct rho and mu
# Increase resolution something funny freeeze lack of motion
# Wrap around though?
# Maybe no Mickey shape?
# More variable dependant
# Make script to launch vscode and terminal stuff