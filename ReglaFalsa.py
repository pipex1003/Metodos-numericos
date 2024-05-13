#MÉTODO DE REGLA FALSA
import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return (x**5-7*x**4+3*x**3-5*x**2+10*x-4)
x = np.arange (-0.5, 6.8, 0.1)

#Definimos una función para hallar las raices
def Reglafalsa(xl, xu):
    ed = 100
    cx = 0
    xr = 0
    i = 0
    iterar = 800
    while( ed > 10**-12 and i <= iterar and f(xr) != 0):
        xr = xu - ( (f(xu)*(xl-xu) ) / (f(xl)-f(xu)))
        ed = abs( (xr -cx)/xr)*100
        
        if( f(xr)*f(xl) < 0 ):
            xu = xr
        else:
            xl = xr
        #
        cx = xr
        i = i + 1
            
    print('   La raiz es: ',xr,'- Error: ',ed,' Iteración: ',i)
    print(f(xr))
    return xr

print('Raíz #1')
Raiz1 = Reglafalsa(0 , 0.6) #Primera Raiz
print('\nRaíz #2')
Raiz2 = Reglafalsa(0.6 , 1) #Segunda Raiz
print('\nRaíz #3')
Raiz3 = Reglafalsa(6 , 7)   #Tercera Raiz

plt.plot(x, f(x))
plt.axhline(0)
plt.axvline(0)
plt.grid()
plt.show()