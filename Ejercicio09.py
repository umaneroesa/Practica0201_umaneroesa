#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
cantidad = float(input("¿Que cantidad quiere invertir? "))
interes = float(input("¿Cuanto tiene de interes anual? "))
años = int(input("¿Durante cuantos años? "))
c = (cantidad*interes*años)+cantidad
print("El capital obtenido en la inversion es de ", c)