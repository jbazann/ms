import numpy as np
#
# DESPLAZAMIENTOS
#
dx2 = 0.5/1e4 # s
dx3 = 2/1e4 # s
#
# FUNCIONES
#
def c(x):
    return 1
def x1(x):
    return x
def x2(x):
    return x*x
def x3(x):
    return x**3
def x4(x):
    return x**4
def x5(x):
    return x**5
def x6(x):
    return x**6
def x7(x):
    return x**7
def x8(x):
    return x**8
def x9(x):
    return x**9
def x10(x):
    return x**10
def x11(x):
    return x**11
def sin(x):
    return np.sin(x)
def cos(x):
    return np.cos(x)

# 2a
# APROXIMACION SINUSOIDAL MINIMOS CUADRADOS
#
def func_min_cuadr_pol():
    return [x11,x10,x9,x8,x7,x6,x5,x4,x3,x2,c]

def aprox1Z(func,p):
    Z = []
    for p0 in p:
        Z.append([])
        for f0 in func:
            Z[-1].append(f0(p0))
    return Z
def aprox1COEF(coef,p):
    aprx = [] 
    func = func_min_cuadr_pol() #
    for p0 in p:
        t = 0
        for i in range(len(coef)):
            t = t + coef[i]*func[i](p0)
        aprx.append(t)
    return aprx

    

