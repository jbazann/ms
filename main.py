from matplotlib import pyplot as plt
import min_cuad as f
import min_cuad_sympy as ms
import numpy as np

import datos as d

def main():
    min_cuad_sin()

def min_cuad_sin():
    n = 50
    x, y = d.medido()
    func, c = d.min_cuad_sin(x,y,n)
    print(c)
    plt.plot(x,ms.eval(c*func,x))
    plt.plot(x,y,'.')
    plt.show()

def min_cuad_sympy():
    gr = 20
    x, y = d.medido()
    for gr in range(5,10):
        c = d.min_cuad_pol(x,y,gr)
        plt.plot(x,ms.eval(c*ms.pol_gr(gr),x))
    c = d.min_cuad_pol(x,y,gr)
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


