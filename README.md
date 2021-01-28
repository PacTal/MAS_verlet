# MAS_verlet
This program solve the  one-dimensional harmonic oscillator using the Verlt's metho.
# -*- coding: utf-8 -*-
from numpy import *                                    
from pylab import *
#from math import *        #---Importa todas las funciones matemáticas--
#import matplotlib.pyplot as plt
"""Mi primer millón PacTal UC-UJTL
   Este programa ejemplifica la conservación de la energía para 
   para un movimiento armónico simple con el algoritmo de verlet.
"""
#-------Parámetros-Unidades MKS-----
PI,Dt,m,k= 3.1415,0.001,0.2,1.3   
T =2.0*PI*sqrt(m/k) #Tiempo máximo de observación en segundos.
Tmax = 1.0*T         #Tiempo máximo de observación en segundos.
#--Condiciones iniciales-Unidades MKS---------
Tiempo = arange(0.,Tmax,Dt) #--Lista que almacena los datos de tiempo para gráficar.
Ec,Ep,Em=[],[],[]  #--Listas que almacena los datos de energía para gráficar.
xo,vo =1.,0.      #---xo posición inicial y vo velocidad inicial.
x,v,t=xo,vo,0.      #--Define la posición, velocidad y tiempo, asigna las condiciones iniciales.
def a(x):return -k*x/m #--Define el método de aceleración.
xm=xo-vo*Dt       #--Primer paso de verlet

for t in Tiempo:
	Ec.append(0.5*m*v*v) #--Calcula la energía cinetica del sistema.Enteros  Ec.append(y) orden por defecto 0.5*m*v*v
	Ep.append(0.5*k*x*x)  #--Calcula la energía potancial del sistema.
	Em.append(0.5*m*v*v+0.5*k*x*x)  #--Calcula la energía mecánica del sistema.
	xx=2.0*x-xm+a(x)*Dt*Dt          #--xx se esta definiendo aquí.
	v=(xx-xm)/(2.0*Dt) 
	xm=x
	x=xx
print("Terminé con exito")
#-----------------GRÁFICAS--------------------------------------------
figure()
plot(Tiempo,Ec,color="red", linewidth=3.0, linestyle=":",label="$E_c$") # má fácil 
plot(Tiempo,Ep,color="green", linewidth=1.5, linestyle="--",label="$E_p$") # "-."
plot(Tiempo,Em,color="blue", linewidth=1.5,label="$E_m$") # 
plt.legend(loc='upper right') # Hace la leyenda de la gráfica loc='upper left'
plt.grid(True)  #--pone una cuadricula
plt.text(5.2, 0.55, r'$\mu=100,\ \sigma=15$',fontsize=18)
xlabel('$t(s)$',fontsize=18)
ylabel( '$E(J)$',fontsize=20)
title( 'Motion Simple Hamonic')
show()
#Estilos de linea
#http://www.thetechrepo.com/main-articles/469-how-to-change-line-properties-in-matplotlib-python.html  
"""
'upper right'  : 1,
'upper left'   : 2,
'lower left'   : 3,
'lower right'  : 4,
'right'        : 5,
'center left'  : 6,
'center right' : 7,
'lower center' : 8,
'upper center' : 9,
'center'       : 10,
"""
