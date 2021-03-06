
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
r1, (x1, y1) = 1, (2, 3)                       # Circle 1, Radius and Center
r2, (x2, y2) = 1, (5, 3)                         # Circle 2, Radius and Center
n = 64                                           # Number of Points
spring_const = 5000                              # Spring Constant
rest_length = round(r1*sqrt(2-2*cos(2*pi/n)), 3) # Rest Length (recommended listed)
Rigidity = 4000000                               # Beam Rigidity
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

# Adding partial points
###############################################

# File output
file_out.write(f"{n + n} # INACCURATE number of vertices in file\n")

for point in circ_1 + circ_2:
    file_out.write(f"{b10(point[0])} {b10(point[1])}\n")

file_out.write("# x-coord, y-coord\n")

print(f"Success: ~/{folder_name}/fila_256.vertex")
file_out.close()

##########################################################################################
#################################### Spring Formation ####################################
##########################################################################################

file_out = open(f"./{folder_name}/fila_256.spring", "w")

file_out.write(f"{n + n + sm_center + 1} # INACCURATE number of springs in file\n")

for x in range(n):
    file_out.write(f"{x%n} {(x+1)%n} {b10(spring_const)} {b10(rest_length)}\n")

for x in range(n):
    file_out.write(f"{n + (x%n)} {n + (x+1)%n} {b10(spring_const)} {b10(rest_length)}\n")

###### PULL BARS #####
for x in range(-1*n//16 ,n//16 + 1):
    pullbar_len_formula = 0.7 - 0.05*abs(x) # <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- <-- 
    print(pullbar_len_formula)
    file_out.write(f"{n//2 - 3*x} {x%n} {b10(spring_const//10)} {b10(pullbar_len_formula)}\n")

###  CONNECTING BARS ###

for x in range(1,5*n_sm//16):
    file_out.write(f"{n//16 + x} {n + n//2 - n//4 - x} {b10(spring_const)} {b10(0.2)}\n")
for x in range(1,5*n_sm//16):
    file_out.write(f"{(-n//16 - x)%n} {n + n//2 + n//4 + x} {b10(spring_const)} {b10(0.2)}\n")

file_out.write("# idx1, idx2, spring constant, rest length\n")
file_out.close()

print(f"Success: ~/{folder_name}/fila_256.spring")

##########################################################################################
##################################### Beam Formation #####################################
##########################################################################################

file_out = open(f"./{folder_name}/fila_256.beam", "w")

file_out.write(f"{7*n//8+n-1} # INACCURATE number of beams in file\n")

for x in range(n):
    file_out.write(f"{x%n} {(x+1)%n} {(x+2)%n} {b10(Rigidity)}\n")
# \/ is for the beamless center
#for x in range(n_big//16 + 1, 15*n_big//16):
#    file_out.write(f"{x%n_big} {(x+1)%n_big} {(x+2)%n_big} {b10(Rigidity)}\n")
for x in range(n):
    file_out.write(f"{n+x%n} {n+(x+1)%n} {n+(x+2)%n} {b10(500000000)}\n")

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

# Touching wall had adverse effects
# Big bounds that fixed previous problem slowed simulation down
# I can literally just hit reopen
# Why did it just go around and work though I don't get it

# TODO try removing pull bars, move further back? Shorter pull bars?
# Two cells, given that environment what does it take to maintain that cleft?
# Add wall-springs
# Translate to 3d
# Too stretchy?
# Change spring constant of pull bars, check input2d to make sure nothing is overwritten
    # Future, have secretory cleft already existing
    # Retrieve output from Visit?
        # SAMRAI Documentation check prob
        
# Get to Rho/Mu
# https://documen.tician.de/pyvisfile/
# https://github.com/inducer/pyvisfile/blob/master/examples/read-qmesh.py
# https://github.com/inducer/pyvisfile
# http://swjones.github.io/resources/pyvisfile
# parse silo files

# External Force, Get to Rho/Mu, and PyVisfile, Permeability, getting output (if pyvisfile doesn't work)
# VisIT command line interface?

"""
Moving towards biophysical design of the scenario
	1. Fix that little thing that happens, maybe by stiffening the springs inside the left cell
	We want to reach equilibrium for both cells x30 or x100
	Use as condition for new simulation
	2. Make it so Mu and Rho (Fluid Viscosity and Fluid Mass Density) are same as reality
		Mu and Rho of Water
		Mu and time can be whatever unit I want (Currently corresponds to seconds?)
	make cell bigger, like 5 times bigger
	Mu should be fine as is
	Rho want Rho = 10^-9 (right now 10^-4), but smaller means way more computational time
		10^-6 is limit for Jonathan's experience
	Can you get it to run up to 0.1 seconds in a day or so?
	Springs between cells should rest at 0.01 m (but try 0.1)
Copy all this information into vim-notes for UCI
Equilibrium shape (final time step)
	Start new simulation, create small half moon. If we restart there, it might go down to the way it was 
	How long until it goes back to equilibrium?
Direction 2: Take to 3d 
Direction 3: Take the whole thing and put in into an HPC
	UCI's HPC3 is shutting down and restarting on December, push it into future
If one cell was pushed against another, will a cleft form, and what's the probability?
	Missing two things
	1. External Force
	2. Springs that only SOMETIMES exert force.
		IRL springs only engage when they get close
	... which is why we should do the first goal of answering "how long"
"""

"""Set up oval, test so its not so... wobbly?, lower rho Keep track of how much expanding/shrinking at any time"""

"""
How are 3d files input structured?
"""