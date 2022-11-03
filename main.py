from matplotlib import pyplot as plt
import min_cuad as f
import min_cuad_sympy as ms

import datos as d

def main():
    min_cuad_sympy()

def mejor_grado(): # busca el polinomio que mejor ajuste al pico de sobre-excitación, a mayor grado mayor oscilacion en pico refractario
    x, y = d.medido()
    mj = 99999
    mjgr = 0
    for gr in range(10,25):
        c = d.min_cuad_sympy(x,y,gr)
        k = ms.eval(c*ms.pol_gr(gr),[0.00199])
        if 26.5 - k[0] < mj:
            mj = 26.5 - k[0]
            mjgr = gr
    print(mjgr)

def min_cuad_sympy():
    gr = 20
    x, y = d.medido()
    c = d.min_cuad_sympy(x,y,gr)
    plt.plot(x,ms.eval(c*ms.pol_gr(gr),x))
    c = d.min_cuad_sympy(x,y,gr)
    plt.plot(x,y,'.')
    plt.show()

def plot_entrada():
    x, y = d.medido()
    plt.plot(x,y,'.')
    plt.show()

    x, y = d.modelo()
    plt.plot(x,y)
    plt.show()

main()


