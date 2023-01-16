"""Este es un ejemplo para una aplicacion en python con funciones que resuelven 
diferentes ejercicios de programacion"""

from math import pi

#Calcula el area de un circulo
def areacirculo(r):
	return pi*r**2

#Convierte grados Farenheit a cenlcius
def farenheitacelcius(f):
	return (f-32)*(5/9)

#Retorna la extension de un archivo
def extensionarchivo(filename):
	split = filename.split(".")
	return split[-1]

#Retorna is un numero dado es par o impar
def esparoimpar(n):
	mod = n % 2
	if mod > 0:
		return "impar"
	else:
		return "par"

def valorascii(c):
	return ord(c)

if __name__ == "__main__":
	print("hola")
	r=1.1
	a=areacirculo(r)
	print("El area de un cirtulo de radio "+str(r)+"  es "+str(a))
	f=32
	c=farenheitacelcius(f)
	print(str(f)+" grados Farenheit son "+str(c)+" grados celcius")
