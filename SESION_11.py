# SESIÓN 11 - PERCEPTRÓN | TALLER DE LABORATORIO: HACKEANDO LOS PESOS
import numpy as np

# Paso 1: código del perceptrón
def funcion_escalon(z):
    if z >= 0:
        return 1
    else:
        return 0

def perceptron(X, W, b):
    Z = np.dot(X, W) + b
    salida = funcion_escalon(Z)
    return salida

# Paso 2: verificar la compuerta AND
pesos = np.array([0.5, 0.5])
sesgo = -0.8
print("--- Compuerta AND (pesos=[0.5, 0.5], sesgo=-0.8) ---")
for entrada in ([1, 0], [0, 1], [0, 0], [1, 1]):
    print(entrada, "->", perceptron(np.array(entrada), pesos, sesgo))

# Pasos 3 y 4: reto, modificar pesos y/o sesgo para resolver la compuerta OR
pesos = np.array([0.5, 0.5])
sesgo = -0.3
print("\n--- Compuerta OR (pesos=[0.5, 0.5], sesgo=-0.3) ---")
for entrada in ([0, 0], [0, 1], [1, 0], [1, 1]):
    print(entrada, "->", perceptron(np.array(entrada), pesos, sesgo))

# Paso 5: valores que resuelven el OR
print("\nPesos:", pesos, "| Sesgo:", sesgo)
