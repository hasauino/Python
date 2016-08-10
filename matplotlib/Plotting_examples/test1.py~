"""
Demo of a simple plot with a custom dashed line.

A Line object's ``set_dashes`` method allows you to specify dashes with
a series of on/off lengths (in points).
"""
from numpy import linspace,sin,array,size,append,power,trapz
from math import pi,exp
from matplotlib.pyplot import plot,show
from scipy.integrate import simps

x=array([10,20,30, 40, 50, 60, 70, 80, 90, 100, 55, 57, 60 ,56 ,80 ,14 ,70 ,35 ,23 ,0 ,40])
u=sum(x)/size(x)

i=0
s=0.0

for i in range(0,size(x)): 
	s+=(x[i]-u)**2
	
sigma2=s/size(x)
sigma=sigma2**0.5

i=0
h=[]

x=linspace(-200,200)
for i in range(0,size(x)):
	h=append(h,((2*pi*sigma2)**-0.5)*exp(-0.5*  ((x[i]-u)**2)/sigma2) )
	
plot(x,h,'-*')
print simps(h,x)
show()

