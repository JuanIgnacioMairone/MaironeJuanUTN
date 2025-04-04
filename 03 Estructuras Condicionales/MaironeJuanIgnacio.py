from statistics import mode, median, mean
import random


#Actividad 1: Mayoria de edad.
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad.")
else: 
    print("No es mayor de edad.")

#Actividad 2: Aprobado/Desaprobado.
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado.")
else:
    print("Desaprobado.")

#Actividad 3: Numeros pares.
numero = int(input("Ingrese un número par: "))
if numero % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")

#Actividad 4: Categorias por edad.
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#Actividad 5: Validacion de contraseña.
contraseña = input("Ingrese una contraseña (8-14 caracteres): ")
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Actividad 6: Analisis estadistico.
numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
else:
    print("Sin sesgo")

#Actividad 7: Frases que terminan en vocal.
texto = input("Ingrese una frase o palabra: ")
vocales = {'a', 'e', 'i', 'o', 'u'}
if texto[-1].lower() in vocales:
    print(texto + "!")
else:
    print(texto)

#Actividad 8: Transformacion de nombres.
nombre = input("Ingrese su nombre (solo letras y espacios): ")

# Validación 1: Rechazar si el nombre contiene números
if any(caracter.isdigit() for caracter in nombre):
    print("Error al ingresar su nombre. Ingrese su nombre utilizando solo letras y espacios.")
else:
    # Validación 2: Opción de formato
    opcion = input("Elija opción (1: MAYÚSCULAS, 2: minúsculas, 3: Primera mayúscula): ")
    
    if opcion == '1':
        print(nombre.upper())
    elif opcion == '2':
        print(nombre.lower())
    elif opcion == '3':
        print(nombre.title())
    else:
        print("Opción no válida")

#Actividad 9: Escala de Richter.
magnitud = float(input("Ingrese magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve")
elif 3 <= magnitud < 4:
    print("Leve")
elif 4 <= magnitud < 5:
    print("Moderado")
elif 5 <= magnitud < 6:
    print("Fuerte")
elif 6 <= magnitud < 7:
    print("Muy fuerte")
else:
    print("Extremo")

#Actividad 10: Estaciones del año.
hemisferio = input("¿En qué hemisferio está? (N/S): ").upper()
mes = int(input("Ingrese mes (1-12): "))
dia = int(input("Ingrese día: "))

if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20):
    estacion = "Invierno" if hemisferio == "N" else "Verano"
elif (mes == 3 and dia >= 21) or (mes <= 6 and dia <= 20):
    estacion = "Primavera" if hemisferio == "N" else "Otoño"
elif (mes == 6 and dia >= 21) or (mes <= 9 and dia <= 20):
    estacion = "Verano" if hemisferio == "N" else "Invierno"
else:
    estacion = "Otoño" if hemisferio == "N" else "Primavera"

print(f"Estación actual: {estacion}")