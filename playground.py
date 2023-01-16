"""Este es un ejemplo para una aplicacion en python con funciones que resuelven 
diferentes ejercicios de programacion"""

from math import pi


def areacirculo(r):
	return pi*r**2

def farenheitacelcius(f):
	return (f-32)*(5/9)

def extensionarchivo(filename):
	split = filename.split(".")
	return split[-1]

def esparoimpar(n):
	mod = n % 2
	if mod > 0:
		return "par"
	else:
		return "impar"

if __name__ == "__main__":
	print("hola")
	r=1.1
	a=areacirculo(r)
	print("El area de un cirtulo de radio "+str(r)+"  es "+str(a))
	f=32
	c=farenheitacelcius(f)
	print(str(f)+" grados Farenheit son "+str(c)+" grados celcius")
