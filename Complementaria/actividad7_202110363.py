import numpy as np

def S(x):
	x = np.array(x)
	return np.sum(x)

def SS(x):
	x = np.array(x)
	return np.sum(x**2)

def SXY(x,y):
	x = np.array(x)
	y = np.array(y)
	return np.sum(x*y)

def delta_x(x):
	n = len(x)
	x = np.array(x)
	return (n * SS(x)) - (S(x))**2

def pendiente(x,y):
	n = len(x)
	return ((n * SXY(x,y)) - (S(x) * S(y))) / delta_x(x)

def punto_corte(x,y):
	return ((SS(x) * S(y)) - (S(x) * SXY(x,y))) / delta_x(x)

def incertidumbre_y(x,y):
	pendiente = pendiente(x,y)
	punto = punto(x,y)
	x = np.array(x)
	y = np.array(y)
	n = len(x)
	return np.sqrt(SS(y - (punto - pendiente*x)) / n - 2)

def incertidumbre_punto(x,y):
	return incertidumbre_y(x,y) * (np.sqrt(SS(x)) / delta_x(x))

def incertidumbre_pendiente(x,y):
	n = len(x)
	return (incertidumbre_y(x,y) * n) / delta_x(x)

def ajuste(x,y):
	return f"y={round(pendiente(x,y),4)}x+{round(punto_corte(x,y),4)}"

def valor_y(x,X,Y):
	m = pendiente(X,Y)
	a = punto_corte(X,Y)
	x = np.array(x)
	return (m * x) + a