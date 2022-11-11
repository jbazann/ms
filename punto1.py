from matplotlib import pyplot as plt
import datos as d
import numpy as np
import sympy as s
from sympy.abc import x
import scipy.interpolate as interpol

def puntoA():
    intervalos()

def puntoB():
    x,y = d.modelo()
    spl = splines()
    rng = arangeSplines()
    y0=interpol.splev(rng,spl)
    plt.plot(x,y,marker='o',markerfacecolor='blue',linestyle='None')
    plt.plot(rng,y0,color='red')
    plt.show()


def splines():
    x,y = d.modelo()
    z=interpol.splrep(x,y,k=3)
    #z2=interpol.splrep(x,y,k=5)

    #arreglo=np.arange(x[0],x[-1],33.3e-6)#No se si esta bien eso
    #zn=interpol.splev(arreglo,z)
    #plt.plot(x,y,marker='o',markerfacecolor='blue',linestyle='None')
    #plt.plot(arreglo,zn,color='red')
    #plt.show()
    return z

def intervalos():
    px,py = d.modeloDerivadas()
    seleccionIntervalos(px,py)

def arangeSplines():
    x,y = d.modelo()
    spacing = 33.3e-6 # intervalo de muestreo arbitrario
    return np.arange(x[0],x[-1],spacing)

def evalSpline(rng,spl):
    return interpol.splev(rng,spl)

def seleccionIntervalos(px,py):
    iX = seleccion(px)
    iY = seleccion(py)
    expresiones=[]
    args=[]
    for i in range(len(iX)):
        expresiones.append(diferenciasDivididas(iX[i],iY[i],i))
        args.append([x,iX[i][0],iX[i][-1]])
    s.plot(*zip(expresiones,args))

def mostrarFuncion(px, py):
    plt.grid(True)
    plt.plot(px,py,marker='o')
    plt.show()

def diferenciasDivididas(x,y,n):
    dD = []
    coef = []
    coef.append(y[0])
    n=n-1
    derivadas=[0, 32.01666667, 128.2565608, 197.1565608, 0, -143.5000000, 0, 2.988571429, 6.467936508,-6.012063492]#Completar con las derivadas
    
    #Si los valores de x son iguales es pq agregamos la derivada
    #Si los valores de x son iguales produce excepcion
    for j in range(len(x)-1):
        if(j == 0):
            for i in range(len(x)-1):
                try:
                    valor = (y[i+1]-y[i])/(x[i+1]-x[i])
                except:
                    #reemplazamos por la derivada
                    valor = derivadas[n]
                dD.append(valor)
        else:
            dD1=[]
            for i in range(len(dD)-1):
                try:
                    valor = (dD[i+1]-dD[i])/(x[i+j+1]-x[i])
                except:
                    #reemplazamos por la derivada
                    valor = derivadas[n]
                dD1.append(valor)
            dD = dD1
        coef.append(dD[0])
    expresion=polinomio(coef,x)
    return expresion

def polinomio(coef,px):
    x = s.Symbol('x')
    expresion = ''
    for i in range(len(coef)):
        if(i==0):
            expresion=expresion+str(coef[i])#Agrega el TI
        else:
            if coef[i]>0:
                expresion=expresion+'+'+str(coef[i])#Agrega el Coeficiente
                for j in range(i):#Agrega los(x-xa)
                    expresion=expresion+'*(x-'+str(px[j])+')'
            elif coef[i]<0:
                expresion=expresion+str(coef[i])#Agrega el Coeficiente
                for j in range(i):#Agrega los(x-xa)
                    expresion=expresion+'*(x-'+str(px[j])+')'
            else:
                expresion=expresion#Deberia agregar 0 pero no aporta nada
    return expresion

def seleccion(x):
    intervalos = [0,1,4,8,11,13,15,18,21,24,27,30] # un intervalo entre cada elemento de la lista, extremos incluidos
    segmentos = []
    cantIntervalos = 11
    i = 0
    k = 1
    while i < cantIntervalos:
        seg = []
        for k in range(intervalos[i],intervalos[i+1]+1):
            seg.append(x[k])
        segmentos.append(seg)
        i+=1
    return segmentos