import numpy as np

#f(r)
def f(r, R=3.884*(10**8), G=6.674*(10**-11), w=2.662*(10**-6), m=7.348*(10**22), M=5.975*(10**24))->float:
    f = (r**5)-((R*2)*(r**4))+((R**2)*(r**3))-(((G/(w**2))*(M-m))*(r**2))+(((2*G*M*R)/(w**2))*(r))-((G*M*(R**2))/(w**2))
    return f

#f'(r)
def fp(r, R=3.884*(10**8), G=6.674*(10**-11), w=2.662*(10**-6), m=7.348*(10**22), M=5.975*(10**24))->float:
    fp = (5*(r**4))-(4*(2*R)*(r**3))+(3*(R**2)*(r**2))-(2*((G/(w**2))*(M-m))*r)+((G*M*(R**2))/(w**2))
    return fp

#Newton-Raphson
def newton(x0=0.5, error=10**(-4)):
    r_distance = x0 - (f(x0) / fp(x0))
    tmp = x0
    while (np.abs(r_distance-tmp) > error):
        tmp = r_distance
        r_distance = r_distance - ((fp(r_distance) / fp(r_distance)))
    return r_distance

print(newton())