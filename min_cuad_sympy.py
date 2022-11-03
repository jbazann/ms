from sympy.abc import x

def pol_gr(gr):
    pol = []
    for i in range(gr+1):
        pol.append(x**i)
        
    return pol

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










