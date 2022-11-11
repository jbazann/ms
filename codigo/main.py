import punto1 as p1
import punto2 as p2

# NOTA IMPORTANTE
# Algunas funciones tienen distintas "configuraciones" para producir distintas gráficas/resultados
# hay que cambiar las lineas comentadas para cambiar los resultados
# ver por ejemplo graficarSplines() en este mismo documento
# por favor no nos quiten puntos por esto no sabemos programar en python somos tontos

def main():
    p1.puntoA()
    p1.puntoB()
    p2.aproxFourier()
    p2.aproxFilt()
    graficarSplines() # en punto2.py hay suficientes funciones para obtener equivalentes a estas dos lineas para la 
    pCritSplines() # aproximación del punto 2, referirse a NOTA IMPORTANTE sobre por qué no existe una función que lo haga

def pCritSplines():
    spl = p1.splines()
    puntos = p2.puntosCriticosSplines(spl)
    print(puntos)

def graficarSplines():
    #T = 'Intersecciones con y = -70 [mV]'
    T = 'Ceros de la derivada'
    spl = p1.splines()
    spl = p2.derSpline(spl)
    rng = p1.arangeSplines()
    vals = p1.evalSpline(rng,spl)
    linea = [0 for v in rng]
    #linea = [-70 for v in rng]
    rng = [r/1e4 for r in rng]
    p2.plot(rng,vals,T)
    p2.plot(rng,linea,T)
    p2.show()

main()


