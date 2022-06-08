#%%

import numpy as np

def f(x):
    return np.exp(-x**2)

def integral_riemann(a=0, b=1, n=1000000):
    i = 0
    fx = 0
    while i <= (n - 1):
        delta_x =   (b - a) / n
        xi = a + (i * delta_x)
        fa = f(xi) * delta_x
        fx += fa
        i += 1
    return fx
print("Punto 1:")
print(integral_riemann())

def test1():
    try:
        assert np.abs(integral_riemann()-0.746824132812427)<1e-6
        print("Resultado Correcto")
    except:
        print("Resultado Incorrecto")
test1()

def integral_trapecio(a=0, b=1, n=1000000):
    i = 0
    fx = 0
    delta_x = (b - a) / n
    while i<= (n - 1):
        xi = a + (i * delta_x)
        fa = f(xi)
        i += 1
        fx += fa
    sum = (delta_x) * ((f(0) / 2) + (f(n) / 2) + fx)
    return sum
print("Punto 2:")
print(integral_trapecio())

def test2():
    try:
        assert np.abs(integral_trapecio()-0.746824132812427)<1e-6
        print("Resultado Correcto")
    except:
        print("Resultado Incorrecto")
test2()
# %%
