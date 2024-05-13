#PUNTO FIJO
#pip install scipy
import math

x = float(input("Introduzca el valor inicial: "))
xo = x
i = 0
n = 10000
e = 0.01
e_a = 1

def f(x):
    return math.exp(x) -5*x
def h(x):
    return math.log(5 * x)

while( ( e_a > e ) and ( i < n ) and ( f(x) != 0 ) ):
    x_e = x
    x = h(x)
    e_a = abs( (x - x_e) / x ) * 100
    i = i + 1

print( '\n'"Punto Fijo ")
print( "La función exp (x) - 5x ")
print("La raiz es", x)
print( "f(raiz) = ",f(x))
print('El error es = ', e_a)
print( 'En la iteración = ', i, '\n')

import scipy.optimize as opt
print("Raiz optimizada PF : ", opt.fixed_point(f,xo,(),e))