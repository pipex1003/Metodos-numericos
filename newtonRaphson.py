import sympy as sym
#pip install sympy 
x = sym.Symbol('x')
xr = float(input("Introduzca el valor inicial: "))
xr= xr
i = 0
n = 10000
e = pow(10,-12)
e_a = 1

f = -2*x**4-1.2*x**4+10*x+5
df = f.diff(x)

if(f.subs(x,xr) != 0):
    while( ( e_a > e ) and ( i < n ) and ( f.subs(x,xr) != 0 ) ):
        xe = xr
        xr = xr - (f.subs(x,xr)/(2*(df.subs(x,xr))))
        e_a = abs( (xr - xe) / xr )*100
        i = i + 1
    print( '\n'"Newton-Raphson ")
    print( "La función :", f)
    print( "La Derivada :", df)
    print("La raiz es : ", xr)
    print( "f(raiz) = ",f.subs(x,xr))
    print('El error es = ', e_a)
    print( 'En la iteración = ', i, '\n')
else:
    print( 'El valor de la raíz es : ', xr)