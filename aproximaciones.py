import math
print("El valor de pi según math es: ",math.pi)
n = 1000
def leibnz(n):
    terminos = ((-1) ** i / (2 * i + 1) for i in range(n))
    aproximacion_pi = 4 * sum(terminos)
    return aproximacion_pi 
aprox_pi1 = leibnz(n)
print("Aproximación de pi con formula leibnz: ",aprox_pi1)
error_leib=math.pi-aprox_pi1
print("el error calculado con la formula leibnz: ",error_leib)

n=1000
def euler(n):
    termino1=((2**i)*((math.factorial(i)**2))/(math.factorial(2*i+1)) for i in range(n))
    aproximacion_euler= 2*sum(termino1)
    return aproximacion_euler
aprox_euler1=euler(n)
print("aproximacion de pi con formula euler: ",aprox_euler1)
error_e=math.pi-aprox_euler1
print("el error calculado con la formula euler: ",error_e)

n=1000
def nilakantha(n):
    aprox = 3 
    aux = 1
    for i in range(1, n + 1):
        termino2 = (4 /((2*i)*(2*i+1)*(2*i+2)))
        aprox += termino2*aux
        aux *= -1 
    return aprox
aprox_nil = nilakantha(n)
print("Aproximación de pi con nilakantha : ",aprox_nil)
error_nil=math.pi-aprox_nil
print("el error calculado con la formula nilkantha: ",error_nil)

def menor_error(error_e,error_leib,error_nil):
    if(error_e<error_leib):
        return print("el menor error es el de euler que es igual a: ",error_e)
    elif (error_leib<error_nil):
        return print("el menor error es el de leibnz que es igual a: ",error_leib)
    elif (error_nil<error_e):
        return print("el menor error es el de leibnz que es igual a: ",error_leib)

print(menor_error(error_e,error_leib,error_nil))

