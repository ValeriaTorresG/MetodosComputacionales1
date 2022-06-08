#%%
import numpy as np
import sympy as sy

#* Creacion de matrices de listas
A = [[1,2,3],[4,5,6]]
B = [[6,5,4],[3,2,1]]
C = [[1,2],[3,4],[5,6]]
D = [[1,2],[3,4]]
E = [[2,2],[2,6]]
F = [[1,1],[1,8]]
k = np.pi

#* funcion que convierte las listas en arrays con Numpy
def crear_array(A):
    return np.array(A)

#* Funcion que convierte la lista en matriz con Numpy
def crear_matriz(A):
    return np.matrix(A)

#* Funcion que convierte la lista en matriz con Sympy
def crear_matriz_sy(A):
    return sy.Matrix(A)

#? Operaciones principales con numpy
def suma(A,B):
    A = crear_array(A)
    B = crear_array(B)
    return np.add(A,B)

def resta(A,B):
    A = crear_array(A)
    B = crear_array(B)
    return A-B

def producto_por_escalar(k,A):
    A = crear_array(A)
    return k*A

def producto(A,B):
    A = crear_array(A)
    B = crear_array(B)
    try:
        return np.dot(A,B)
    except:
        return None

def inversa(A):
    A = crear_matriz(A)
    try:
        adj = A.getH()
        t = adj.transpose()
        det = np.linalg.det(A)
        return (t/det).transpose()
    except:
        return None

def determinante(A):
    A = np.matrix(A)
    return np.linalg.det(A)

def resolver_sistema(A,B):
    try:
        A_inversa = np.linalg.inv(A)
        x = np.dot(A_inversa, B)
        return x
    except:
        return "No tiene solución en los reales"

#? Comprobaciones con Sympy
def comprobar_suma(A,B):
    A = crear_matriz_sy(A)
    B = crear_matriz_sy(B)
    return A+B

def comprobar_resta(A,B):
    A = crear_matriz_sy(A)
    B = crear_matriz_sy(B)
    return A-B

def comprobar_producto_por_escalar(k,A):
    A = crear_matriz_sy(A)
    return k*A

def comprobar_producto(A,B):
    try:
        A = crear_matriz_sy(A)
        B = crear_matriz_sy(B)
        return A@B
    except:
        return None

def comprobar_inversa(A):
    try:
        A = crear_matriz_sy(A)
        return A.inv()
    except:
        return None

def comprobar_determinante(A):
    A = crear_matriz_sy(A)
    return A.det()

def comprobar_resolver_sistema(A,B):
    try:
        A = crear_matriz_sy(A)
        A_inversa = A.inv()
        B = crear_matriz_sy(B)
        return A_inversa@B
    except:
        return "No tiene solución en los reales"

#! Imprimir resultados
"""print("1. Suma") #!FUNCIONA
print(f"Numpy:\n{suma(A,B)}")
print(f"Sympy:\n{comprobar_suma(A,B)}")
print("\n")

print("2. Resta") #!FUNCIONA
print(f"Numpy:\n{resta(A,B)}")
print(f"Sympy:\n{comprobar_resta(A,B)}")
print("\n")

print("3. Producto por escalar") #!FUNCIONA
print(f"Numpy:\n{producto_por_escalar(k,A)}")
print(f"Sympy:\n{comprobar_producto_por_escalar(k,A)}")
print("\n")

print("4. Producto punto") #!FUNCIONA
print(f"Numpy:\n{producto(A,C)}")
print(f"Sympy:\n{comprobar_producto(A,C)}")
print("\n")
"""
print("5. Matriz inversa") #!NO FUNCIONA
print(f"Numpy:\n{inversa(D)}")
print(f"Sympy:\n{comprobar_inversa(D)}")
print("\n")

"""print("6. Determinante") #!FUNCIONA
print(f"Numpy:\n{determinante(D)}")
print(f"Sympy:\n{comprobar_determinante(D)}")
print("\n")

print("7. Resolver sistema de la forma Ax=B") #!FUNCIONA, HABÍA PROBLEMA CON LA MATRIZ DE PRUEBE
print(f"Numpy:\n{resolver_sistema(E,F)}")
print(f"Sympy:\n{comprobar_resolver_sistema(E,F)}")
print("\n")"""
# %%
