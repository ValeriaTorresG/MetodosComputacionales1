#%%

#Importación de modulos
import numpy as np
import sympy as sym
import pandas as pd
import matplotlib.pyplot as plt

#funcion que calcula el polinomio y puntos de Lagrange, y grafica los puntos
def pol(car:str):
    datos = pd.read_csv("vapor_saturado.csv", delimiter=";")

    n = len(datos)
    x = sym.Symbol("x")
    i = 0
    polinomio = 0

    for i in range(0,n,1):
        num = 1
        den = 1
        for j in range(0,n,1):
            if (i != j):
                num = num * (x-datos[car][j])
                den = den * (datos[car][i] - datos[car][j])
            termino = num / den
        polinomio = polinomio + termino

    px = sym.lambdify(x, polinomio)
    a = np.min(datos[car])
    b = np.max(datos[car])
    muestras = 10000
    p_xi = np.linspace(a,b,muestras)
    pfi = px(p_xi)

    print(f"{car} vs. T")
    plt.plot(datos[car], datos['temp'], 'o', label=f"{car}")
    plt.plot(p_xi, pfi)
    plt.title(f"{car} vs. T")
    plt.show()
    plt.savefig(f"{car}vsT.png")


def PvsT():
    pol('salt_press')
PvsT()

def VgvsT():
    pol('sat_liquid')
VgvsT()

def VfvsT():
    pol('sat_vapor')
VfvsT()

"""
#ANALISIS DE RESULTADOS


#CONLUSIONES


"""
# %%
