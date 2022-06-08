
import numpy as np
matrix = np.array([[3,-1,-1,0,0,0,5],
                  [-1,4,-1,-1,0,0,5],
                  [0,-1,-1,4,-1,-1,0],
                  [0,0,-1,-1,4,-1,0],
                  [0,0,0,-1,-1,3,0],
                  [-1,-1,4,-1,-1,0,5]])

def find_system(matrix):
    A = []
    for i in matrix:
        temp = []
        for j in range(0,5,1):
            temp.append(i[j])
        A.append(temp)
    A = np.array(A)
    b = []
    for i in matrix:
        b.append(i[6])
    b = np.array(b)
    return (A,b)

def find_voltages(matrix):
    solved = matrix.copy().astype(float)
    n = solved.shape[0]
    for i in range(n):
        for j in range(i+1, n):
            solved[j] = (solved[j, i] / solved[i, i]) * solved[i] - solved[j]
    solved = solved.copy().astype(float)
    n = solved.shape[0]
    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            solved[j] = (solved[j, i] / solved[i, i]) * solved[i] - solved[j]
        solved[i] = solved[i] / solved[i, i]
    x = []
    for i in solved:
        x.append(i[6])
    x = np.array(x)
    return x

A, x, b = find_system(matrix)[0], find_voltages(matrix), find_system(matrix)[1]
"""print(A)
print("\n")
print(x)
print("\n")
print(b)
print("\n")"""
#%%
import numpy as np
def resistance():
    r = 0
    matrix = np.array([[0,0,1,1],
                      [0,0,2,1],
                      [0,0,2,1],
                      [0,0,2,1],
                      [0,0,2,1],
                      [0,0,2,1],
                      [1,1,0,0]])
    for i in matrix:
        for j in i:
            if j == 1:
                r += 1
            elif j == 2:
                temp = r/(r+1)
                r = temp
            else:
                pass
    return r

print(resistance())



# %%
