import sympy as s
from sympy.abc import x

def pol_gr(gr):
    pol = []
    for i in range(gr+1):
        pol.append(x**i)
        
    return pol

def nsincos(n):
    freq = 1/0.006
    func = [s.sin(0*x+s.pi*0.5)]
    for i in range(1,n):
        func.append(s.sin(i*freq*x))
        func.append(s.cos(i*freq*x))
    return func


def min_cuad_Z(func,p):
    Z = []
    for p0 in p:
        Z.append([])
        for f0 in func:
            Z[-1].append(f0.subs(x,p0))
    return Z

def eval(func,p):
    val = []
    for p0 in p:
        tot = 0
        for f0 in func:
            tot += f0.subs(x,p0)
        val.append(tot)
    return val










