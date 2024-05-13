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

    error_bi = abs(b - a) / 2.0
    return c, error_bi, iteracion
a = -550
b = 550
tolerancia = 1e-11
max_iter = 10000
raiz, error_bi, iteracion = biseccion(a, b, tolerancia, max_iter)
print(f"Raiz estimada con biseccion: {raiz}")
print(f"Error verdadero: {error_bi}")
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
            error_rf = abs(b - a) / 2
            return c, error_rf, iteracion

        if fa * fc < 0:
            b = c
        else:
            a = c

    error_rf = abs(b - a) / 2
    return c, error_rf, iteracion
a = -550
b = 550
tolerancia = 1e-12
max_iteraciones = 10000
raiz, error_rf, iteracion = regla_falsa(a, b, tolerancia, max_iteraciones)
print(f"Raíz aproximada con regla falsa: {raiz}")
print(f"Error verdadero: {error_rf}")
print(f"Iteración: {iteracion}")



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

    error_n = abs(funcion(x_actual))
    return x_actual, error_n, iteracion

valores_iniciales = [-4, 0, 4, 5, 7, 8]

tolerancia = 1e-12
max_iter = 10000

for valor_inicial in valores_iniciales:
    raiz, error_n, iteracion = newton_raphson(valor_inicial, tolerancia, max_iter)
    print(f"Para X={valor_inicial}:")
    print(f"Raiz estimada con newton: {raiz}")
    print(f"Error verdadero: {error_n}")
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

    error_s = abs(funcion(x1))
    return x1, error_s, iteracion

# Valores iniciales para el método de la secante
x0 = -550
x1 = 550

# Especificar la tolerancia y el número máximo de iteraciones
tolerancia = 1e-11
max_iter = 10000

# Aplicar el método de la secante
raiz, error_s, iteracion = secante(x0, x1, tolerancia, max_iter)

# Imprimir resultados
print(f"Raiz estimada con secante: {raiz}")
print(f"Error verdadero con secante: {error_s}")
print(f"Iteraciones: {iteracion}")

def menor_error(error_bi,error_rf,error_n,error_s):
    if(error_bi<error_rf and error_bi<error_n and error_bi<error_s):
        return print("el menor error es el de biseccion que es igual a: ",error_bi)
    elif (error_rf<error_bi and error_rf<error_n and error_rf<error_s):
        return print("el menor error es el de regla falsa que es igual a: ",error_rf)
    elif (error_n<error_bi and error_n<error_rf and error_rf<error_s):
        return print("el menor error es el de newton que es igual a: ",error_n)
    else:
        return print("el menor error es el de secante que es igual a: ",error_s)
print(menor_error(error_bi,error_rf,error_n,error_s))

#punto fijo----------------------------------------------------
def g1(x):
    numerator = 3.54*x**6 - 2.2129*x**5 + 5.5716*x**4 + 0.1004*x**3 - 15.3991*x**2 - 6.7827*x - 0.76176
    denominator = x if abs(x) > 1e-10 else 1e-10  # Evitar divisiones por valores cercanos a cero
    return numerator / denominator

def g2(x):
    numerator = x**7 + 2.2129*x**5 - 5.5716*x**4 + 0.1004*x**3 - 15.3991*x**2 - 6.7827*x - 0.76176
    denominator = 3.54 if abs(3.54) > 1e-10 else 1e-10  # Evitar divisiones por valores cercanos a cero
    return numerator / denominator

def g3(x):
    numerator = x**7 - 3.54*x**6 + 2.2129*x**5 + 5.5716*x**4 + 0.1004*x**3 - 15.3991*x**2 - 6.7827*x
    denominator = 0.76176 if abs(0.76176) > 1e-10 else 1e-10  # Evitar divisiones por valores cercanos a cero
    return numerator / denominator

def punto_fijo(g, intervalo, tolerancia, max_iter):
    a, b = intervalo
    x_inicial = (a + b) / 2.0
    iteracion = 0

    while abs(g(x_inicial) - x_inicial) > tolerancia and iteracion < max_iter:
        x_inicial = g(x_inicial)
        iteracion += 1

    error_verdadero = abs(g(x_inicial) - x_inicial)
    return x_inicial, error_verdadero, iteracion

# Intervalos iniciales para el método de punto fijo
intervalo1 = (-550,550)
intervalo2 = (-1, 100)
intervalo3 = (-2, 5)

# Especificar la tolerancia y el número máximo de iteraciones
tolerancia = 1e-12
max_iter = 10000

# Aplicar el método de punto fijo para cada despeje
raiz1, error1, iteracion1 = punto_fijo(g1, intervalo1, tolerancia, max_iter)
raiz2, error2, iteracion2 = punto_fijo(g2, intervalo2, tolerancia, max_iter)
raiz3, error3, iteracion3 = punto_fijo(g3, intervalo3, tolerancia, max_iter)

# Imprimir resultados
print("Para el despeje 1:")
print(f"Raiz estimada: {raiz1}")
print(f"Error verdadero: {error1}")
print(f"Iteraciones: {iteracion1}")
print("------")

print("Para el despeje 2:")
print(f"Raiz estimada: {raiz2}")
print(f"Error verdadero: {error2}")
print(f"Iteraciones: {iteracion2}")
print("------")

print("Para el despeje 3:")
print(f"Raiz estimada: {raiz3}")
print(f"Error verdadero: {error3}")
print(f"Iteraciones: {iteracion3}")

