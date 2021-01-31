#Import libraries	
from numpy import *
import math
import matplotlib.pyplot as plt

"""
This function will plot each particle 
"""

def plot():
	v = float(input("\tWrite the velocity for particle       "))
	q = -float(input("\tWrite the charge for particle       "))
	d = 0.0001
	m = 9.10938291*(10**-31)
	V = 1*(10**-15)
	l = int(input("\tWrite the angle       "))
	t= linspace(0,10,15)
	ecuation = ((+(((-q*V)/(d*m))*t*t))/10) +l

	#plot the data as scatter points
	plt.plot(t,ecuation,'r')
	plt.ylabel('y-axis in meters')
	plt.xlabel('x-axis in meters')
	plt.title('Trayectory')

#Ask for how many particles we want
particles = int(input("How many particles you want to generate       "))
for i in range(0,particles):
	print("\nParticle " + str(i+1) + ":       ")
	plot()
plt.show()