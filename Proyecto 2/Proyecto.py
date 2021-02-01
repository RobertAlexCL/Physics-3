import matplotlib.pyplot as plt
import numpy
import math


B = 1
voltage = 1
e = 1.602176634*math.pow(10,-19)
particulas = [(e, 1.67262192369*math.pow(10,-27), 'Protón'), (2*e, 6.644657230*math.pow(10,-27), 'Partícula alfa'), (-e,9.10938291*math.pow(10,-31), 'Electrón')
              ,(e,9.10938291*math.pow(10,-31), 'Positrón'), (-e,3.167*math.pow(10,-27), 'Tau')]
#Formato particulas: (carga , masa, nombre)
#menu
print('Puede seleccionar una de las siguientes partículas')
numero = 0
for carga,masa,nombre in particulas:
    numero = numero + 1
    print('Partícula número: ' + str(numero) )
    print('Nombre: ' + nombre)
    print('Carga: ' + str(carga))
    print('Masa: ' + str(masa))
    print()
print('Ingrese los numeros de las particulas que desea usar en el siguiente formato: ')
print('1,2,3 esto usaría un protón, una partícula alfa y un electrón')
print('También puede ingresar 6 para ingresar una partícula personalizada con la cantidad de electrones, protones y neutrones que desee')
seleccion = input()
seleccion = seleccion.split(',')
seleccionadas = []
for selec in seleccion:
    if int(selec) == 6:
        print('Ingrese la cantidad de electrones:')
        elec = int(input())
        print('Ingrese la cantidad de protones:')
        prot = int(input())
        print('Ingrese la cantidad de neutrones:')
        neut = int(input())
        particulas.append(((prot-elec)*e,
                           1.67262192369*math.pow(10,-27)*(prot+neut) + 9.10938291*math.pow(10,-31)*elec,
                           'Personalizada con ' + str(elec) + ' e-, ' + str(prot) + ' p+ y ' + str(neut) + ' n'))
    seleccionadas.append(particulas[int(selec)-1])
print('Ingrese el voltage el selector')
voltage = float(input())
velocidad = numpy.sqrt(e*voltage/9.10938291*math.pow(10,-31))
for carga,masa,nombre in seleccionadas:
    x = []
    y = []
    for t in numpy.linspace(0, numpy.pi, 100):
        R = masa*velocidad/(carga*B)
        x.append(R-R*numpy.cos(t))
        if (carga < 0):
            R = -R
        y.append(R*numpy.sin(t))
        
    plt.plot(x, y)
    plt.title(nombre)
    plt.xlabel('Distancia recorrida (metros)')
    plt.ylabel('Distancia recorrida (metros)')
    plt.show()