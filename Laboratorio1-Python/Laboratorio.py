print(''.join(reversed('!Hola Mundo!'))) #Ejercicio 1

s = '!Hola Mundo!' #Ejercicio 2
print(''.join(reversed(s)))

print('Cual es tu nombre?') #Ejercicio 3
name = input()
print('!Hola ' + name + '!')

print(((3+2)/(2*5))**2) #Ejercicio 4

h = float(input('Ingrese el numero de horas trabajadas: ')) #Ejercicio 5
c = float(input('Ingrese el coste por hora: '))
r = h * c
print('La paga es ', r)

n = int(input("Ingrese un numero entero positivo: ")) #Ejercicio 6
suma = n * (n+1) / 2
print('La suma de todos los enteros desde 1 hasta ' + str(n) + ' es ' + str(suma))

peso = input("Cual es tu peso(en kg) ? ") #Ejercicio 7
estatura = input("Cual es tu estatura(en metros) ?")
imc = round(float(peso)/float(estatura)**2,2)
print("Tu indice de masa corporal es " + str(imc))

x = input("Introduce el dividendo (entero): ") #Ejercicio 8
y = input("Introduce el divisor (entero): ")
print(x + " entre " +  y + " da un cociente " + str(int(x) // int(y)) + " y un residuo de " + str(int(x) % int(y)))

cantidad = float(input("¿Cantidad a invertir? ")) #Ejercicio 9
interes = float(input("¿Interes porcentual anual? "))
years = int(input("¿Años?"))
print("Capital final: " + str(cantidad * (interes / 100 + 1) ** years))

p_payaso = 112 #Ejercicio 10
p_muneca = 75
payasos = int(input("Ingrese el numero de payasos a enviar: "))
munecas = int(input("Ingrese el numero de muñecas a enviar: "))
p_total = p_payaso * payasos + p_muneca * munecas
print("El peso total del paquete es " + str(p_total))