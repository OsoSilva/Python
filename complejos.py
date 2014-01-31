#!/usr/bin/python
# -*- encoding: utf-8 -*-

import cmath
from math import degrees

def modulo(n):
	lol = cmath.sqrt((n.real**2)+(n.imag**2))
	return lol.real

def fase(n):
	return degrees(cmath.phase(complex(n.real,n.imag)))

def potencia(n,m):
	return n**m

def suma(n,m):
	return n+m

def resta(n,m):
	return n-m

def multiplicacion(n,m):
	return n*m

def division(n,m):
	return n/m

def main():
	while True:
		switch={
			1:modulo,
			2:fase,
			3:potencia,
			4:suma,
			5:resta,
			6:multiplicacion,
			7:division,
		}
		print """
			[CALCULADORA]

			Elige una opción
			[1] Módulo de un número
			[2] Fase de un número
			[3] Potencia de un número (n^m)
			[4] Suma de dos números
			[5] Resta de dos números
			[6] Multiplicación de dos números
			[7] División de dos números
			[8] Salir
		"""
		opc = input("> ")
		if(opc>=1 and opc<=2):
			try:
				n = input("Numero> ")
				x = switch[opc](n)
				print "Resultado: "+str(x)+"\n"
			except:
				print "Número no válido"
		elif(opc>2 and opc<8):
			try:
				n = input("n> ")
				m = input("m> ")
				x = switch[opc](n,m)
				print "Resultado: "+str(x)+"\n"
			except:
				print "Número(s) no válido(s)"
		elif(opc==8):
			exit()
main()
