import random

import numpy

f = open("matrix.txt", "r")

length = int(f.readline())
mat = [[0 for c in range(length)] for r in range(length)]

for index, line in enumerate(f):
    lines = line.split()
    for idx, element in enumerate(lines):
        element = int(element)
        mat[index][idx] = element

def partA():
    count = 0;
    mNew = [[0 for c in range(length)] for r in range(length)]
    for index, col in enumerate(mat):
        for idx, row in enumerate(mat):
            if mat[index][idx] == 1:
                count += 1
        for idx, row in enumerate(mat):
            if mat[index][idx] == 1:
                mNew[index][idx] = float(1/count)
        count = 0
    mNew = numpy.transpose(mNew)
    # print(mNew)

    v = [1/length for c in range(length)]

    for c in range(30):
        k = numpy.matmul(mNew, v)
        v = k
        # print(v)

    return v

def partB(m,n):
    A = []
    visiter = [0 for c in range(length)]
    for i in range(m):
        rand = random.randint(0, length - 1)
        for j in range(n):

            for mm in range(i):
                rand = random.randint(0, length - 1)
                for nn in range(j):
                    for idx, num in enumerate(mat):
                        if mat[rand][idx] == 1:
                            A.append(idx)
                    rand = A[random.randint(0, len(A) - 1)]
                    visiter[rand] += 1
    for idx, visit in enumerate(visiter):
        visiter[idx] = visiter[idx]/(length*m*n)

    return visiter

a = partA()


z = [0 for c in range(length)]
print("Vector from part A:", a)

b = partB(5,5)
for idx, k in enumerate(z):
    z[idx] = b[idx] - a[idx]
print("l1 error for m = 5, n = 5 is: ", z)

b = partB(10,10)
for idx, k in enumerate(z):
    z[idx] = b[idx] - a[idx]
print("l1 error for m = 10, n = 10 is: ", z)

b = partB(50,50)
for idx, k in enumerate(z):
    z[idx] = b[idx] - a[idx]
print("l1 error for m = 50, n = 50 is: ", z)

b = partB(100,100)
for idx, k in enumerate(z):
    z[idx] = b[idx] - a[idx]
print("l1 error for m = 100, n = 100 is: ", z)




