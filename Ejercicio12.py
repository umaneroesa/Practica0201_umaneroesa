#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y la ganancia final total.
barras = int(input("Numero de barras vendidas que no son del dia: "))
precio = 3.49 
descuento = 0.6
coste = barras * precio * (1 - descuento)
gan=(round(coste, 2))
print("Una barra fresca cuesta ",precio, end='€\n')
print("El descuento sobre una barra no fresca es de ", (descuento * 100), end='%\n')
print("La ganancia final es ", gan, end='€\n')