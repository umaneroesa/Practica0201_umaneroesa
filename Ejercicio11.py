#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
dinero = float(input("Cantidad de dinero ingresado"))
interes = 0.04
año1 = dinero * (1 + interes)
C1=round(año1, 2)
print("Cantidad de ahorro tras el primer año es de ", C1)
año2 = año1 * (1 + interes)
C2=round(año2, 2)
print("Cantidad de ahorro tras el segundo año es de ", C2)
año3 = año2 * (1 + interes)
C3=round(año3, 2)
print("Cantidad de ahorro tras el segundo año es de ", C3)