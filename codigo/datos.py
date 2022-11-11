import numpy as np
import min_cuad_sympy as ms

duracion_medido = 6/1e3 # s
muestreo_modelo = 33.33/1e6 # s

def modeloDerivadas():
    x = []
    modelo = []
    with open('Potencial de acción modelo derivadas.txt') as f:
        for l in f:
            t = l.partition(';')
            x.append(parsefloat(t[0]))
            modelo.append(parsefloat(t[2]))
        f.close()
    return [x,modelo]

def medido():
    x = []
    medido = []
    with open('Potencial de acción medido.txt') as f:
        for l in f:
            t = l.partition(';')
            x.append(int(t[0]))
            medido.append(parsefloat(t[2])) 
        f.close()
    frecuencia_medicion = 1/duracion_medido
    mediciones = len(x)
    x = [x0/(frecuencia_medicion*mediciones) for x0 in x]
    return [x,medido]

def modelo():
    x = []
    modelo = []
    with open('Potencial de acción modelo.txt') as f:
        for l in f:
            t = l.partition(';')
            x.append(parsefloat(t[0]))
            modelo.append(parsefloat(t[2]))
        f.close()
    return [x,modelo]

def parsefloat(s):
    return float(s.strip().replace(',','.'))
