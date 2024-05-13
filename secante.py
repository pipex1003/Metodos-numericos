#SECANTE
import math

x_0 = int(input("Introduzca el extremo inferior del intervalo: "))
x_1 = int(input("Introduzca el extremo superior del intervalo: "))
x_2= x_0 + x_1
i = 0
n = 10000
e = pow(10,-12)
e_a = 1

def f(x):
    return math.exp(x)- 5*x

if( f(x_2) != 0):
    while( ( e_a > e ) and ( i < n ) and ( f(x_2) != 0 ) ):
        x_2 = x_1 - ( ( f(x_1)*f(x_1 - x_0)) / (f(x_1)-f(x_0)) )
        e_a = abs( (x_2 - x_1) / x_2 )*100
        x_0 = x_1
        x_1 = x_2
        i = i + 1
    print( '\n'"Secante")
    print( "La función exp(x) -5x:")
    print("La raiz es : ", x_2)
    print( "f(raiz) = ",f(x_2))
    print('El error es = ', e_a)
    print( 'En la iteración = ', i, '\n')
else:
    print( 'El valor de la raíz es : ', x_2)