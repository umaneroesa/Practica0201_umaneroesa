#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
Horas = int(input('¿Cuantas horas has trabajado?'))
Coste = float(input('¿Cuanto cuesta la hora?'))
sueldo = Horas * Coste
print('Te corresponde una paga de ', sueldo, end='€\n')