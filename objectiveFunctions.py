import math

def paracaidist_speed(coeff):
	mass=68.1
	time=10
	speed=40
	return ((9.8*mass)/coeff)*(1-math.exp((-coeff/mass)*time)) - speed