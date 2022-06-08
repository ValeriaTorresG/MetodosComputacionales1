#%%

from scipy.integrate import quad
import numpy as np

#*PUNTO 3
def f(x):
    return ((np.sin(x))**2)*(np.sqrt(100*x))
def gauss_integrate(n, a=0, b=1):
    xi, wi = np.polynomial.legendre.leggauss(n)
    u = (b-a)*xi/2+(a+b)/2
    integral = ((b-a)/2)*np.sum(wi*f(u))
    return integral
#print(gauss_integrate(4))
def verify_gauss_integrate():
    x = lambda x: f(x)
    return(quad(x, 0, 1)[0])
#print(verify_gauss_integrate())

#!PUNTO 2
import numpy as np
def f(x,y):
    if (x**2+y**2) <= 1:
        return np.sqrt(1-(x**2)-(y**2))
    else:
        return 0
def volume_semisphere(n)->float:
    grid = np.ndarray((n+1,n+1), dtype=np)
    mean = np.ndarray((n,n), dtype=np)
    a = 0
    for i in range(0,n+1,1):
        b = 0
        for j in range(0,n+1,1):
            xy = (a,b)
            b += 2/n
            print(i,j)
            grid[i][j] = xy
            grid[i][j] = round((f(grid[i][j][0],grid[i][j][1])), 2)
        a += 2/n
    area = (2/n)**2
    for k in range(0,n,1):
        for l in range(0,n,1):
            if k<n and l<n: #no calcula bien el promedio de los vértices
                mean[k][l] = ((grid[k][l]+grid[k+1][l]+grid[k][l+1]+grid[k+1][l+1])/4)*area
            elif k<n and l==n:
                mean[k][l] = ((grid[k][l]+grid[k-1][l]+grid[k][l+1]+grid[k-1][l+1])/4)*area
            elif k==n and l<n:
                mean[k][l] = ((grid[k][l]+grid[k+1][l]+grid[k][l-1]+grid[k+1][l-1])/4)*area
    #volume_sphere = np.sum(mean)
    return 0#volume_sphere

#print(f"Volume semisphere with n = 2: {volume_semisphere(2)}")
#print(f"Volume semisphere with n = 3: {volume_semisphere(3)}")
print(f"Volume semisphere with n = 10: {volume_semisphere(10)}")
#print(f"Volume semisphere with n = 100: {volume_semisphere(100)}")

# %%
