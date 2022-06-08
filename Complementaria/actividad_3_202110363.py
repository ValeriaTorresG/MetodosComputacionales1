import numpy as np
import matplotlib.pyplot as plt


#------------------------------------------------------------------------
#!Calculo derivadas

#Implementacion de la funcion f(x)
def f(x, n, A = 1, A1 = 1, A2 = 1):
    if n == 1:
        return ((A1 / x**6) - (A2 / (x**12)))
    elif n == 2:
        return (A * np.cos(x))

#Derivada hacia adelante de la funcion f(x)
def derivada_adelante(x, n, h):
    return ((f(x + h, n) - f(x, n)) / h)

#Derivada hacia atras de la funcion f(x)
def derivada_atras(x, n, h):
    return ((f(x, n) - f(x - h, n)) / h)

#Derivada centrada de la funcion f(x)
def derivada_centrada(x, n, h):
    return ((f(x + h, n) - f(x - h, n)) / (2 * h))


#------------------------------------------------------------------------
#!Graficas f(x) = (1/x^6)-(1/x^12)

#Grafica f(x)
def grafica_f1():
    x = np.linspace(0.01, 10, 100)
    n = 1
    h = 0.1
    print("1) f(x)=(1/x^6)-(1/x^12)")
    plt.plot(x, f(x, n), label = "f(x)")
    plt.title("f(x) = (1/x^6)-(1/x^12)")
    plt.legend()
    plt.show()
    plt.savefig("grafica_f1.png")
grafica_f1()

#Grafica derivada hacia adelante
def grafica_df_adelante_1():
    x = np.linspace(0.01, 10, 100)
    n = 1
    h1 = 0.1
    df = derivada_adelante(x, n, h1)
    print("Derivada hacia adelante h = 0.1")
    plt.plot(x, df, label = "derivada_adelante")
    plt.title("f(x) = (1/x^6)-(1/x^12)")
    plt.legend()
    plt.show()
    plt.savefig("Derivada_1era_funcion_adelante1.png")
    h2 = 0.2
    df = derivada_adelante(x, n, h2)
    print("Derivada hacia adelante h = 0.2")
    plt.plot(x, df, label = "derivada_adelante")
    plt.title("f(x) = (1/x^6)-(1/x^12)")
    plt.legend()
    plt.show()
    plt.savefig("Derivada_1era_funcion_adelante2.png")
grafica_df_adelante_1()

#Grafica derivada hacia atras
def grafica_df_atras_1():
    x = np.linspace(0.01, 10, 100)
    n = 1
    h1 = 0.1
    df = derivada_atras(x, n, h1)
    print("Derivada hacia atras h = 0.1")
    plt.plot(x, df, label = "derivada_atras")
    plt.title("f(x) = (1/x^6)-(1/x^12)")
    plt.legend()
    plt.show()
    plt.savefig("Derivada_1era_funcion_atras1.png")
    h2 = 0.2
    df = derivada_atras(x, n, h2)
    print("Derivada hacia atras h = 0.2")
    plt.plot(x, df, label = "derivada_atras")
    plt.title("f(x) = (1/x^6)-(1/x^12)")
    plt.legend()
    plt.show()
    plt.savefig("Derivada_1era_funcion_atras2.png")
grafica_df_atras_1()

#Grafica derivada centrada
def grafica_df_centrada_1():
    x = np.linspace(0.01, 10, 100)
    n = 1
    h1 = 0.1
    df = derivada_centrada(x, n, h1)
    print("Derivada centrada h = 0.1")
    plt.plot(x, df, label = "derivada_centrada")
    plt.title("f(x) = (1/x^6)-(1/x^12)")
    plt.legend()
    plt.show()
    plt.savefig("Derivada_1era_funcion_central1.png")
    h2 = 0.2
    df = derivada_centrada(x, n, h2)
    print("Derivada centrada h = 0.2")
    plt.plot(x, df, label = "derivada_centrada")
    plt.title("f(x) = (1/x^6)-(1/x^12)")
    plt.legend()
    plt.show()
    plt.savefig("Derivada_1era_funcion_central2.png")
grafica_df_centrada_1()


#------------------------------------------------------------------------
#!Graficas f(x) = Acos(x)

#Grafica f(x)
def grafica_f2():
    x = np.linspace(0.01, 10, 100)
    n = 2
    print("2) f(x) = Acos(x)")
    plt.plot(x, f(x, n), label = "f(x)")
    plt.title("f(x) = Acos(x)")
    plt.legend()
    plt.show()
    plt.savefig("grafica_f2.png")
grafica_f2()

#Grafica derivada hacia adelante
def grafica_df_adelante_2():
    x = np.linspace(0.01, 10, 100)
    n = 2
    h1 = 0.1
    df = derivada_adelante(x, n, h1)
    print("Derivada hacia adelante h = 0.1")
    plt.plot(x, df, label = "derivada_adelante")
    plt.title("f(x) = Acos(x)")
    plt.legend()
    plt.show()
    plt.savefig("Derivada_2da_funcion_adelante1.png")
    h2 = 0.2
    df = derivada_adelante(x, n, h2)
    print("Derivada hacia adelante h = 0.2")
    plt.plot(x, df, label = "derivada_adelante")
    plt.title("f(x) = Acos(x)")
    plt.legend()
    plt.show()
    plt.savefig("Derivada_2da_funcion_adelante2.png")
grafica_df_adelante_2()

#Grafica derivada hacia atrás
def grafica_df_atras_2():
    x = np.linspace(0.01, 10, 100)
    n = 2
    h1 = 0.1
    df = derivada_atras(x, n, h1)
    print("Derivada hacia atras h = 0.1")
    plt.plot(x, df, label = "derivada_atras")
    plt.title("f(x) = Acos(x)")
    plt.legend()
    plt.show()
    plt.savefig("Derivada_2da_funcion_atras1.png")
    h2 = 0.2
    df = derivada_atras(x, n, h2)
    print("Derivada hacia atras h = 0.2")
    plt.plot(x, df, label = "derivada_atras")
    plt.title("f(x) = Acos(x)")
    plt.legend()
    plt.show()
    plt.savefig("Derivada_2da_funcion_atras2.png")
grafica_df_atras_2()

#Grafica derivada centrada
def grafica_df_centrada_2():
    x = np.linspace(0.01, 10, 100)
    n = 2
    h1 = 0.1
    df = derivada_centrada(x, n, h1)
    print("Derivada centrada h = 0.1")
    plt.plot(x, df, label = "derivada_central")
    plt.title("f(x) = Acos(x)")
    plt.legend()
    plt.show()
    plt.savefig("Derivada_2da_funcion_central1.png")
    h2 = 0.2
    df = derivada_centrada(x, n, h2)
    print("Derivada centrada h = 0.2")
    plt.plot(x, df, label = "derivada_central")
    plt.title("f(x) = Acos(x)")
    plt.legend()
    plt.show()
    plt.savefig("Derivada_2da_funcion_central2.png")
grafica_df_centrada_2()


#------------------------------------------------------------------------
#!Derivada de forma analitica
#Derivada analitica f(x) = Acos(x)
def fp1(x = np.linspace(0.01, 10, 100)):
    n = 2
    h = 0.1
    return -np.sin(x)

#Derivada analitica f(x) = (1/x^6)-(1/x^12)
def fp2(x = np.linspace(0.01, 10, 100)):
    n = 2
    h = 0.1
    return ((-6/(x**7))+(12/(x**13)))


#------------------------------------------------------------------------
#!Maximos y minimos
#*cuidado con dividir sobre 0
#Primera derivada de f(x)
def fp(x,n,A1=1,A2=1,A=1):
    if n==1:
        return (-6*A1/x**7+12*A2/x**13)
    if n==2:
        return (-A*np.sin(x))
print(fp(1, 2))

#Segunda derivada f(x)
def fpp(x,n,A1=1,A2=1,A=1):
    if n==1:
        return (6*7*A1/x**8-12*13*A2/x**14)
    if n==2:
        return -A*np.cos(x)
print(fpp(1, 2))

#Metodo de Newton-Raphson
def Newton(x0,n,error):
    xn1=x0-fp(x0,n)/fpp(x0,n)
    tmp=x0
    while(np.abs(xn1-tmp)>error):
        tmp=xn1
        xn1=xn1-fp(xn1,n)/fpp(xn1,n)
        print(xn1)
    return xn1
print(Newton(0.5,1,1e-20))