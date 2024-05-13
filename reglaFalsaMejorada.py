import math

def f(x):
    return ;

def rFalsePlus(xl,xu):
    ea=100 #Error
    i=1
    xold=0
    xr=3
    il=0
    iu=0
    while ea>10**-12 and i<=1000 and f(xr)!=0:
        xr=xu-(f(xu)*(xl-xu))/(f(xl)-f(xu))
        ea=abs(((xr-xold)/xr))*100
        signo=f(xr)*f(xl)
        if signo<0:
            xu=xr
            il++
            iu=0
            if il>=2:
                xl/=2
        else
            xl=xr
            iu++
            il=0
            if iu>=2:
                xu/=2
            

        xold=xr #PlaceHolder
        i+=1
    
    print('Numero de iteraciones por regla falsa mejorada: ',i)
    print('Error por regla falsa mejorada: ', ea)
    print('Raiz por regla falsa: mejorada',xr)
    
