from math import cos, sin, pi, sqrt

Big_Cell = []
Small_Cell = []
for i, line in enumerate(open(f"./fila_256/fila_256.vertex", "r")):
    if i!=0 and i!=129:
        values = [float(s) for s in line.split()]
        if i < 80:
            Big_Cell.append(values)
        else:
            Small_Cell.append(values)

print(Big_Cell)
print(Small_Cell)

def circ(x, y, r, n):                            # Generates Circle coordinates
    return [(cos(2*pi/n*i)*r + x, sin(2*pi/n*i)*r + y)
        for i in range(0,n)]
def b10(num):
    return "{:.10e}".format(num)
    
n = 64
dx = Big_Cell[n//16 + 1][0] - Big_Cell[0][0]
dy = Big_Cell[n//16 + 1][1] - Big_Cell[0][1]
rad = sqrt(dx**2 + dy**2)
print(rad)
mini_circ = circ(Big_Cell[0][0], Big_Cell[0][1], rad, n//4)

for x in range(-1*n//16 ,n//16 + 1):
    Big_Cell[x] = mini_circ[n//8-x]

file_out = open(f"./fila_256/fila_256.vertex", "w")
file_out.write("128 # INACCURATE number of vertices in file\n")

for point in Big_Cell + Small_Cell:
    file_out.write(f"{b10(point[0])} {b10(point[1])}\n")
    
    

        