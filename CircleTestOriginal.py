import math
import os

#folder_name = input("Output Folder Name: ")
folder_name = "3"

try: # Creates folder named folder_name
    os.mkdir(folder_name)
except OSError:
    print ("\nCreation of the directory %s failed / Already Exists\n" % folder_name)
else:
    print ("\nSuccessfully created the directory %s \n" % folder_name)

r1 = 1 # radius 1
x1 = 2 # x coordinate of center 1
y1 = 2 # y coordinate of center 1

r2 = 1 # radius 2
x2 = 5 # x coordinate of center 2
y2 = 2 # y coordinate of center 2

n = 32 # number of points

def tenDig(num): # Turns numbers into the 0.0000000000+e0 format
    return "{:.10e}".format(num)

def genCircle(x,y,r,n):
    return [(math.cos(2*math.pi/n*i)*r + x,math.sin(2*math.pi/n*i)*r + y) for i in range(0,n)]

fout = open ("./" + folder_name + "/fila_256.vertex", 'w')

fout.write(str(n*2) + " "*33 + "# number of vertices in file\n") # Number of vertices in file

# Gets coordinates of points around Circle 1 and Circle 2
Circle1 = genCircle(x1,y1,r1,n)
Circle2 = genCircle(x2,y2,r2,n)

for point in Circle1:
    fout.write(f"{tenDig(point[0])} {tenDig(point[1])}\n")
for point in Circle2:
    fout.write(f"{tenDig(point[0])} {tenDig(point[1])}\n")

fout.write("# x-coord, y-coord\n")

print("fila_256.vertex created in %s \n" % folder_name)
fout.close()

# Creating fila_256.spring

spring_constant = 5 # spring constant

current_length1 = r1 * math.sqrt(2 - 2*math.cos(2*math.pi/n))
current_length2 = r2 * math.sqrt(2 - 2*math.cos(2*math.pi/n))
print(f"Adjacent points are {current_length1} apart (1)")
print(f"Adjacent points are {current_length2} apart (2)")

rest_length = round(current_length1, 1) # Rest Length (recommended above)

fout = open ("./" + folder_name + "/fila_256.spring", 'w')

fout.write(str(2*n + n//2 + 1) + " "*37 + "# number of springs in file\n")

for x in range(n):
    fout.write(f"{x%n} {(x+1)%n} {tenDig(spring_constant)} {tenDig(rest_length)}\n")

for x in range(n):
    fout.write(f"{n + (x%n)} {n + (x+1)%n} {tenDig(spring_constant)} {tenDig(rest_length)}\n")

for x in range(-n//4, n//4 + 1):
    fout.write(f"{x%n} {3*n//2 - x} {tenDig(spring_constant)} {tenDig(rest_length)}\n")

fout.write("# idx1, idx2, spring constant, rest length\n")
fout.close()

print("\nfila_256.spring created in %s" % folder_name)

# Creating fila_256.beam

fout = open ("./" + folder_name + "/fila_256.beam", 'w')

fout.write(f"{2*n} \n")

sciZero = "0.0000000000000000e+00"

for x in range(n):
    fout.write(f"{x%n} {(x+1)%n} {(x+2)%n} {sciZero}\n")
for x in range(n):
    fout.write(f"{n+x%n} {n+(x+1)%n} {n+(x+2)%n} {sciZero}\n")

fout.write("# idx1, idx2, idx3, rigidity\n")
fout.close()