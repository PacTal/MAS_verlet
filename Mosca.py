import matplotlib.pyplot as plt
from pylab import*
Tmax= 50.   #----Tiempo máximo para el experimento virtual
DeltaT=0.01 #----Incremento temporal MUR si es muy pequeño se filtra
va,vb,vm=10.,-10.,100.
#----Cambie esto-----
T,XA,XB,XM=[],[],[],[]
#---Variables
t,xa,xb,xm=0.,0.,100.,0.
Cont=0
while t<= Tmax:
  T.append(t)
  XA.append(xa)
  XB.append(xb)
  XM.append(xm)
  xa=xa+va*DeltaT
  xb=xb+vb*DeltaT
  xm=xm+vm*DeltaT
  if xm>=xb:
    vm=-vm
    xm=xm+vm*DeltaT
    #Cont=Cont+1
  if xm<=xa:
    vm=-vm
    xm=xm+vm*DeltaT
    Cont=Cont+1
  if xa>=xb:break
  t=t+DeltaT

print("Número de choques",Cont)
#---Graficas de posición vs tiempo
plot(T,XA,color="red",label='Tren A')
plot(T,XB,color="blue",label='Tren B')
plot(T,XM,color="green",label='Mosca')
plt.grid(False)
#plt.ylim(0,800)  # rango
#plt.xlim(0,7)  # rango
plt.legend(loc='upper right')  #---lower center, lower right, upper left
ylabel('$x(m)$',fontsize=16)
xlabel('$t(s)$',fontsize=16)
title('La Mosca de Neumann')
show()

