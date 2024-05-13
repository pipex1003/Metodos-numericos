import math
#pip install sympy 
x = float(input("Introduzca el valor inicial: "))
xo= x
x_r = x
i = 0
n = 10000
e = pow(10,-12)
e_a = 1

def f(x):
    return math.exp(x)- 5*x
def df(x):
    return math.exp(x)-5

if( f(x) != 0):
    while( ( e_a > e ) and ( i < n ) and ( f(x_r) != 0 ) ):
        x = x_r
        x_r = x_r - (f(x_r)/(df(x_r)))
        e_a = abs( (x_r - x) / x_r )*100
        i = i + 1
    print( '\n'"Newton-Raphson 2")
    print( "La función exp(x) -5x:")
    print("La raiz es : ", x_r)
    print( "f(raiz) = ",f(x_r))
    print('El error es = ', e_a)
    print( 'En la iteración = ', i, '\n')
else:
    print( 'El valor de la raíz es : ', x)

import scipy.optimize as opt

print('Raiz optimizada N-R: ', opt.newton(f,xo,None,(),e))