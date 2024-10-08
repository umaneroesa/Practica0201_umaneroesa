#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
n = input("Introduce el dividendo (entero): ")
m = input("Introduce el divisor (entero): ")
a = int(n) // int(m)
r = int(n) % int(m)
print(n, " entre ",  m, " da un cociente de ", a, " y un resto de division entera de ", r)