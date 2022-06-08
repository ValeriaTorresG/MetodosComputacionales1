
#!PUNTO 1
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x = [1., 2., 3., 4., 5.]
y = [1.20,  0.31, 3.92, 3.78, 4.47]

def zero(x):
    n = np.sum(np.array(x))
    mean = n / len(x)
    temp = []
    for i in range(0,len(x),1):
        temp.append(mean)
    return np.array(temp)

def linear(x,y):
    dots = []
    for i in range(0,len(x),1):
        temp = []
        temp.append(1)
        temp.append(x[i])
        dots.append(temp)
    x = np.array(dots)
    fit = np.transpose(np.linalg.inv(np.transpose(x)@x))@(np.transpose(x))@(np.array(y))
    return ((fit[1]*np.array(x))+fit[0])[:,1]

def quadratic(x,y):
    x = np.array(x)
    y = np.array(y)
    eq1 = [np.sum(x**2), np.sum(x), len(x)]
    eq2 = [np.sum(x**3), np.sum(x**2), np.sum(x)]
    eq3 = [np.sum(x**4), np.sum(x**3), np.sum(x**2)]
    a = np.array([eq1, eq2, eq3])
    b = np.array([[np.sum(y)], [np.sum(x*y)], [np.sum((x**2)*y)]])
    solved = np.linalg.solve(a,b)
    return (solved[0]*(x**2))+(solved[1]*x)+solved[2]

def cubic(x,y):
    x = np.array(x)
    y = np.array(y)
    eq1 = [np.sum(x**3), np.sum(x**2), np.sum(x), len(x)]
    eq2 = [np.sum(x**4), np.sum(x**3), np.sum(x**2), np.sum(x)]
    eq3 = [np.sum(x**5), np.sum(x**4), np.sum(x**3), np.sum(x**2)]
    eq4 = [np.sum(x**6), np.sum(x**5), np.sum(x**4), np.sum(x**3)]
    a = np.array([eq1, eq2, eq3, eq4])
    b = np.array([[np.sum(y)], [np.sum(x*y)], [np.sum((x**2)*y)], [np.sum((x**3)*y)]])
    solved = np.linalg.solve(a,b)
    return (solved[0]*(x**3))+(solved[1]*(x**2))+(solved[2]*x)+solved[3]

def fourth(x,y):
    x = np.array(x)
    y = np.array(y)
    eq1 = [np.sum(x**4), np.sum(x**3), np.sum(x**2), np.sum(x), len(x)]
    eq2 = [np.sum(x**5), np.sum(x**4), np.sum(x**3), np.sum(x**2), np.sum(x)]
    eq3 = [np.sum(x**6), np.sum(x**5), np.sum(x**4), np.sum(x**3), np.sum(x**2)]
    eq4 = [np.sum(x**7), np.sum(x**6), np.sum(x**5), np.sum(x**4), np.sum(x**3)]
    eq5 = [np.sum(x**8), np.sum(x**7), np.sum(x**6), np.sum(x**5), np.sum(x**4)]
    a = np.array([eq1, eq2, eq3, eq4, eq5])
    b = np.array([[np.sum(y)], [np.sum(x*y)], [np.sum((x**2)*y)], [np.sum((x**3)*y)], [np.sum((x**4)*y)]])
    solved = np.linalg.solve(a,b)
    return (solved[0]*(x**4))+(solved[1]*(x**3))+(solved[2]*(x**2))+(solved[3]*x)+solved[4]


cubic_interpolation_model = interp1d(x, y, kind = "cubic")
X = np.linspace((np.array(x)).min(), (np.array(x)).max(), 500)
Y = cubic_interpolation_model(X)

plt.scatter(x,y, c='mediumpurple')
plt.plot(X, zero(X))
plt.plot(x, linear(x,y))
plt.plot(x, quadratic(x,y))
plt.plot(X, cubic(X,Y), 'red')
plt.plot(X, fourth(X,Y), 'mediumpurple')
plt.title('Matrix Regression Method')
plt.xlabel('x')
plt.ylabel('Y')
#%%
import numpy as np
def num_collisions(m1, m2):
    theta = np.arctan(np.sqrt(m2)/np.sqrt(m1))
    count = 0
    while count * theta < np.pi:
        count += 1
    return count
print(num_collisions(1, 1))
print(num_collisions(10, 1))
print(num_collisions(100, 1))
print(num_collisions(1000, 1))
print(num_collisions(10000, 1))
print(num_collisions(100000, 1))
print(num_collisions(1000000, 1))
print(num_collisions(10000000, 1))
print(num_collisions(100000000, 1))
print(num_collisions(10000000000000000, 1))

#%%%
def num_collisions(m1, m2):
    v1=-1
    v2=0
    count = 0
    while v1 < v2:
        count += 1
        v1_old = v1
        v2_old = v2
        v1 = (v1_old*((m1-m2)/(m1+m2)))+(v2_old*((2*m2)/(m1+m2)))
        v2 = (v1_old*((2*m1)/(m1+m2)))+(v2_old*((m2-m1)/(m1+m2)))
        if v2 < 0:
            count += 1
            v2 = -v2
    return count

import numpy as np
#!PUNTO 3

def num_collisions(m1, m2, v1=-1, v2=0):
    count = 0
    a = np.array([[(m1-m2)/(m1+m2),(2*m2)/(m1+m2)], [(2*m1)/(m1+m2),(m2-m1)/(m1+m2)]])
    b = np.array([[-1,0], [0,1]])
    while not (v1>=0 and v2>=0 and v2>=v1):
        v = np.array([[v1], [v2]])
        if ((np.shape(a)[0]) == (np.shape(v))[1]) and (count % 2 < 1):
            v = np.dot(a,v)
        elif (np.shape(b)[0]) == (np.shape(v))[1]:
            v = np.dot(b,v)
        count += 1
        print(count)
        v1 = v[0]
        v2 = v[1]
        count += 1

    return count

print(num_collisions(1, 1))
print(num_collisions(10, 1))
print(num_collisions(100, 1))
print(num_collisions(1000, 1))
print(num_collisions(10000, 1))
print(num_collisions(100000, 1))
print(num_collisions(1000000, 1))
print(num_collisions(10000000, 1))
print(num_collisions(100000000, 1))

# %%
#!PUNTO 2





# %%
