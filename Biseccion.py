#biseccion--------------------------
def funcion(x):
    return x**7 - 3.54*x**6 + 2.2129*x**5 - 5.5716*x**4 - 0.1004*x**3 + 15.3991*x**2 + 6.7827*x + 0.76176
def biseccion(a, b, tolerancia, max_iter):
    iteracion = 1
    while (b - a) / 2.0 > tolerancia and iteracion <= max_iter:
        c = (a + b) / 2.0
        if funcion(c) == 0.0:
            break
        elif funcion(c) * funcion(a) < 0:
            b = c
        else:
            a = c

        iteracion += 1

    error_verdadero = abs(b - a) / 2.0
    return c, error_verdadero, iteracion
a = -550
b = 550
tolerancia = 1e-11
max_iter = 10000
raiz, error, iteracion = biseccion(a, b, tolerancia, max_iter)
print(f"Raiz estimada con biseccion: {raiz}")
print(f"Error verdadero: {error}")
print(f"Iteraciones: {iteracion}")

#regla falsa-----------------------------
def f(x):
    return x**7 - 3.54*x**6 + 2.2129*x**5 - 5.5716*x**4 - 0.1004*x**3 + 15.3991*x**2 + 6.7827*x + 0.76176

def regla_falsa(a, b, tol, max_iter):
    iteracion = 0

    while iteracion < max_iter:
        iteracion += 1

        fa = f(a)
        fb = f(b)

        c = (a * fb - b * fa) / (fb - fa)

        fc = f(c)

        if fc == 0 or abs(b - a) < tol:
            error_verdadero = abs(b - a) / 2
            return c, error_verdadero, iteracion

        if fa * fc < 0:
            b = c
        else:
            a = c

    error_verdadero = abs(b - a) / 2
    return c, error_verdadero, iteracion


a = -550
b = 550
tolerancia = 1e-12
max_iteraciones = 10000


raiz, error, iteracion = regla_falsa(a, b, tolerancia, max_iteraciones)


print(f"Raíz aproximada con regla falsa: {raiz}")
print(f"Error verdadero: {error}")
print(f"Iteración: {iteracion}")

#punto fijo----------------------------------------------------
def funcion_original(x):
    return x**7 - 3.54*x**6 + 2.2129*x**5 - 5.5716*x**4 - 0.1004*x**3 + 15.3991*x**2 + 6.7827*x + 0.76176

def g1(x):
    return (3.54*x**6 - 2.2129*x**5 + 5.5716*x**4 + 0.1004*x**3 - 15.3991*x**2 - 6.7827*x - 0.76176)**(1/7)

def g2(x):
    return (3.54*x**6 - 2.2129*x**5 + 5.5716*x**4 + 0.1004*x**3 - 15.3991*x**2 - 6.7827*x - 0.76176)**(1/6)

def g3(x):
    return (3.54*x**6 - 2.2129*x**5 + 5.5716*x**4 + 0.1004*x**3 - 15.3991*x**2 - 6.7827*x - 0.76176)**(1/5)

def punto_fijo(g, x_inicial, tolerancia, max_iter):
    iteracion = 1

    while iteracion <= max_iter:
        x_siguiente = g(x_inicial)

        if abs(x_siguiente - x_inicial) < tolerancia:
            break

        x_inicial = x_siguiente
        iteracion += 1

    return x_siguiente, abs(x_siguiente - x_inicial), iteracion


a = -550
b = 550

tolerancia = 1e-6
max_iter = 10000

g_funcion = g1

x_inicial = 1

raiz_punto_fijo, error_punto_fijo, iteracion_punto_fijo = punto_fijo(g_funcion, x_inicial, tolerancia, max_iter)


print(f"Raiz estimada con Punto Fijo: {raiz_punto_fijo}")
print(f"Error verdadero con Punto Fijo: {error_punto_fijo}")
print(f"Iteraciones con Punto Fijo: {iteracion_punto_fijo}")

#newton-------------------------
def funcion(x):
    return x**7 - 3.54*x**6 + 2.2129*x**5 - 5.5716*x**4 - 0.1004*x**3 + 15.3991*x**2 + 6.7827*x + 0.76176

def derivada(x):
    return 7*x**6 - 21.24*x**5 + 11.0645*x**4 - 22.2864*x**3 - 0.3012*x**2 + 30.7982*x + 6.7827

def newton_raphson(x_inicial, tolerancia, max_iter):
    x_actual = x_inicial
    iteracion = 0

    while abs(funcion(x_actual)) > tolerancia and iteracion < max_iter:
        x_actual = x_actual - funcion(x_actual) / derivada(x_actual)
        iteracion += 1

    error_verdadero = abs(funcion(x_actual))
    return x_actual, error_verdadero, iteracion

valores_iniciales = [-4, 0, 4, 5, 7, 8]

tolerancia = 1e-12
max_iter = 10000

for valor_inicial in valores_iniciales:
    raiz, error, iteracion = newton_raphson(valor_inicial, tolerancia, max_iter)
    print(f"Para X={valor_inicial}:")
    print(f"Raiz estimada con newton: {raiz}")
    print(f"Error verdadero: {error}")
    print(f"Iteraciones: {iteracion}")
    
#secante-----------------------
def funcion(x):
    return x**7 - 3.54*x**6 + 2.2129*x**5 - 5.5716*x**4 - 0.1004*x**3 + 15.3991*x**2 + 6.7827*x + 0.76176

def secante(x0, x1, tolerancia, max_iter):
    iteracion = 0

    while abs(funcion(x1)) > tolerancia and iteracion < max_iter:
        x_nueva = x1 - (funcion(x1) * (x1 - x0)) / (funcion(x1) - funcion(x0))
        x0, x1 = x1, x_nueva
        iteracion += 1

    error_verdadero = abs(funcion(x1))
    return x1, error_verdadero, iteracion

# Valores iniciales para el método de la secante
x0 = -550
x1 = 550

# Especificar la tolerancia y el número máximo de iteraciones
tolerancia = 1e-11
max_iter = 10000

# Aplicar el método de la secante
raiz, error, iteracion = secante(x0, x1, tolerancia, max_iter)

# Imprimir resultados
print(f"Raiz estimada con secante: {raiz}")
print(f"Error verdadero con secante: {error}")
print(f"Iteraciones: {iteracion}")
