from matplotlib import pyplot as plt
import scipy.interpolate as interp
import scipy.signal as sig
import numpy as np
import min_cuad_sympy as ms
import datos as d

def aproxFourier():
    #T = 'Aproximación a datos tras filtrado de orden 3'
    T = 'Aproximación mediante serie de Fourier acotada'
    x,y = d.medido()
    Periodo = d.duracion_medido
    n = 10
    frq = 2*np.pi/Periodo
    func = fourier(n,frq)
    #x,y = aproxFilt(x,y)
    fx = min_cuad((x,y),func,T)
    y0 = ms.eval(fx,x)
    plotd(x,y)
    plot(x,y0,T)
    show()

def aproxCheby():
    T = 'Aproximación a mediante polinomios de Chebyshev'
    x,y = d.medido()
    n = 15
    func = cheby(n)
    fx = min_cuad((x,y),func,T)
    y0 = ms.eval(fx,x)
    plotd(x,y)
    plot(x,y0,T)
    show()

def aproxPol():
    T = 'Aproximación a mediante polinomios completos simples'
    x,y = d.medido()
    n = 15
    func = pol_gr(n)
    fx = min_cuad((x,y),func,T)
    y0 = ms.eval(fx,x)
    plotd(x,y)
    plot(x,y0,T)
    show()

def aproxFilt():
    T = 'Aproximación a datos tras filtrado de orden 3'
    x,y = d.medido()
    Periodo = d.duracion_medido
    fs = len(x)/Periodo
    cutoff = 1875
    ord = 3
    y = filtrar(y,cutoff,fs,ord)

    frq = 2*np.pi/Periodo
    n = 10
    func = fourier(n,frq) 

    fx = min_cuad((x,y),func,T)
    y0 = ms.eval(fx,x)
    plotd(x,y)
    plot(x,y0,T)
    show()

def filtrar(data,cutoff,fs,ord):
    normal_cut = cutoff/(0.5*fs)
    b, a = sig.butter(ord,normal_cut,btype='low',analog=False)
    return sig.filtfilt(b,a,data)

def puntosCriticosSplines(spl):
    dspl = interp.splder(spl)
    #evaluar = [[1.9,2.2],[2.8,3.1]]
    evaluar = [[3,2.2]]
    r = []
    for ev in evaluar:
        r.append(raicesSpline(*ev,spl))
    r.append(raicesSplineNewton(1,spl))
    r.append(raicesSplineNewton(4,spl))
    puntos = []
    for p in r:
        y = interp.splev(p,spl)
        puntos.append((p,y))
    return puntos

def raicesSplineNewton(p,spl):
    tol = 1/1e12
    maxit = 30
    ajuste = 70
    fp = interp.splev(p,spl)+ajuste
    dspl = interp.splder(spl)
    m = interp.splev(p,dspl)
    p = -fp/m + p
    res = interp.splev(p,spl)+ajuste
    it = 1
    while abs(res) > tol and it < maxit:
        m = interp.splev(p,dspl)
        p = -res/m + p
        res = interp.splev(p,spl)+ajuste
        it += 1   
    return p

def raicesSpline(p0,p1,spl):
    tol = 1/1e12
    maxit = 30
    ajuste = 70
    fp0 = interp.splev(p0,spl)+ajuste
    fp1 = interp.splev(p1,spl)+ajuste
    m = (fp0 - fp1)/(p0 - p1)
    p = -fp0/m + p0
    res = interp.splev(p,spl)+ajuste
    it = 1
    while abs(res) > tol and it < maxit:
        if res < 0:
            fp0 = res
            p0 = p
        else:
            fp1 = res
            p1 = p
        m = (fp0 - fp1)/(p0 - p1)
        p = -fp0/m + p0
        res = interp.splev(p,spl)+ajuste
        it += 1   
    return p

def cheby(n):
    return ms.cheby(n)

def fourier(n,frq):
    return ms.nsincos2(n,frq)

def pol_gr(gr):
    return ms.pol_gr(gr)

def min_cuad(datos,func,T):
    x, y = datos
    a, b = (x[0],x[-1])
    #x = [2*(x0 - (1/2)*(a+b))/(b-a) for x0 in x] # Para Chebyshev
    c = coef(x,y,func)
    fx = c*func
    #fx[0] += 70 # Para búsqueda de raíces
    return fx

def raices(p0,p1,func):
    tol = 1/1e12
    maxit = 15
    fp0 = ms.eval(func,[p0])[0].evalf()
    fp1 = ms.eval(func,[p1])[0].evalf()
    m = (fp0 - fp1)/(p0 - p1)
    p = -fp0/m + p0
    res = ms.eval(func,[p])[0].evalf()
    it = 1
    while abs(res) > tol and it < maxit:
        if res < 0:
            fp0 = res
            p0 = p
        else:
            fp1 = res
            p1 = p
        m = (fp0 - fp1)/(p0 - p1)
        p = -fp0/m + p0
        res = ms.eval(func,[p])[0].evalf()
        it += 1   
    return p

def coef(x0,y,func):
    Y = y
    Z = ms.min_cuad_Z(func,x0)
    ZT = np.transpose(Z)
    ZTZ = np.dot(ZT,Z)
    ZTY = np.dot(ZT,Y)
    ZTZ = np.array(ZTZ,dtype='float64')
    ZTY = np.array(ZTY,dtype='float64')
    c = np.linalg.solve(ZTZ,ZTY)
    return c

def derSpline(spl):
    return interp.splder(spl)

def plot(x,y,T):
    plt.title(T)
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Potencial Medido [mV]')
    plt.plot(x,y)

def plotd(x,y):
    plt.plot(x,y,'.')

def show():
    plt.show()

def plot_entrada():
    x, y = d.medido()
    plt.plot(x,y,'.')
    plt.show()
    x, y = d.modelo()
    plt.plot(x,y,'.')
    plt.show()
