import matplotlib.pyplot as plt

for fileID in range(11):
    X, Y = [], []
    A, B = [], []
    for i, line in enumerate(open(f"./VisExport/Analysis/{format(fileID, '04')}.txt", "r")):
        values = [float(s) for s in line.split()]
        if i < 80:
            X.append(values[0])
            Y.append(values[1])
        else:
            A.append(values[0])
            B.append(values[1])
    plt.plot(X+[X[0]], Y+[Y[0]])
    plt.plot(A+[A[0]], B+[B[0]])
    plt.show()

