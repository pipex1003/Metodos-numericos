import numpy as np
from scipy.optimize import newton

# Coeficientes del polinomio
coefficients = [1, -63.63, 664.837, 12003.7, -4529.18]

# Definir la función del polinomio y su derivada
def polynomial(x):
    return np.polyval(coefficients, x)

def derivative(x):
    return np.polyder(coefficients)(x)

# Encontrar las raíces usando el método de Newton-Raphson
roots = []
initial_guesses = np.linspace(-10, 10, 5)  # Ajusta los valores iniciales según sea necesario

for guess in initial_guesses:
    root = newton(polynomial, guess, fprime=derivative)
    roots.append(root)

# Mostrar las raíces encontradas
print("Raíces encontradas:", roots)
