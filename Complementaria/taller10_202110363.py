import numpy as np
from regex import P
from scipy.stats import norm
import scipy.stats as stats
import matplotlib.pyplot as plt

def punto_11(n_sample=50, miu=15, miu_sample=14.15, sigma=3):
    z = (miu_sample - miu) / (sigma/np.sqrt(n_sample))
    print(f"a. El valor estadístico de prueba z=(x-miu)/sigma/(n)^1/2) es: {z}")
    p_value = 2 * norm.cdf(miu_sample, loc = miu, scale = sigma/np.sqrt(n_sample))
    print(f"b. El valor -p es de: {p_value}")
    print("c. Usando alpha=0.05 es posible concluir que no corresponde, ya que el valor de -p es menor que el valor de alpha")
    x = np.linspace(-4.5, 4.5)
    y = stats.norm.pdf(x, 0, 1)
    plt.plot(x, y)
    x2 = np.linspace(1.96, 4.5, 50)
    y2 = stats.norm.pdf(x2, 0, 1)
    plt.fill_betweenx(y2,x2, 1.96, color = "blue")
    x3 = np.linspace(-4.5, -1.96, 50)
    y3 = stats.norm.pdf(x3, 0, 1)
    plt.fill_betweenx(y3,x3, -1.96, color = "blue")
    plt.axvline(x=z, color = "red")
    plt.axvline(x=-z, color = "red")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()
    print(f"d. Si se usa la regla de rechazo con valor critico puede concluirse que la hipotesis es nula, ya que se encuentra por fuera del rango, por lo que miu no corresponde")
#punto_11()

def punto_12(n_sample=48, miu=18, miu_sample=17, sigma=4.5):
    z = (miu_sample - miu) / (sigma/np.sqrt(n_sample))
    print(f"a. El valor estadístico de prueba z=(x-miu)/sigma/(n)^1/2) es: {z}")
    p_value = 2 * norm.cdf(miu_sample, loc=miu, scale = sigma/np.sqrt(n_sample))
    print(f"b. El intervalo del valor -p corresponde a: {2} y el valor -p es: {p_value}")
    print("c. Usando alpha=0.05 es posible concluir que si corresponde, ya que el valor de -p es mayor que el valor de alpha")
    x = np.linspace(-4.5, 4.5)
    y = stats.norm.pdf(x, 0, 1)
    plt.plot(x, y)
    x2 = np.linspace(1.96, 4.5, 50)
    y2 = stats.norm.pdf(x2, 0, 1)
    plt.fill_betweenx(y2,x2, 1.96, color = "blue")
    x3 = np.linspace(-4.5, -1.96, 50)
    y3 = stats.norm.pdf(x3, 0, 1)
    plt.fill_betweenx(y3,x3, -1.96, color = "blue")
    plt.axvline(x=z, color = "red")
    plt.axvline(x=-z, color = "red")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()
    print(f"d. Si se usa la regla de rechazo con valor critico puede concluirse que la hipotesis es verdadera, ya que se encuentra dentro del rango, por lo que miu corresponde")
#punto_12()

def punto_3():
    p_value = 0
    conclusion = ""

    sigma = 0.05
    meas_A = [6.24, 6.31, 6.28, 6.30, 6.25, 6.26, 6.24, 6.29, 6.22, 6.28]
    meas_B = [6.27, 6.25, 6.33, 5.27, 6.24, 6.31, 6.28, 6.29, 6.34, 6.27]

    miu = np.sum(meas_A) / len(meas_A)
    mean = np.sum(meas_B) / len(meas_B)

    sigma_mean = sigma / np.sqrt(len(meas_A))
    p_value = 2 * norm.cdf(mean, loc = miu, scale = sigma/np.sqrt(len(meas_A)))
    z = (mean - miu) / sigma_mean

    alpha = 0.05
    if p_value > alpha:
        conclusion = "verdadera"
    else:
        conclusion = "falsa"

    print(p_value)
    print(f"p value = {p_value}, la conclusion es:  {conclusion}")

#punto_3()