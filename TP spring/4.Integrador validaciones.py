'''Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos. 
Los datos requeridos son: 
● Apellido 
● Edad, entre 18 y 90 años inclusive. 
● Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”. 
● Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda. 
Una vez ingresados y validados los datos, mostrarlos por pantalla.'''
# Apellido (no vacío)
apellido = input("Ingresa tu apellido: ")
while apellido == "":
    apellido = input("Ingresa tu apellido: ")

# Edad (entre 18 y 90 inclusive)
edad = int(input("Ingresa tu edad (18-90): "))
while edad < 18 or edad > 90:
    print("Edad inválida. Debe estar entre 18 y 90.")
    edad = int(input("Ingresa tu edad (18-90): "))

# Estado civil (validar opciones)
estado_civil = input("Ingresa tu estado civil (Soltero, Casado, Divorciado, Viudo): ")
while estado_civil not in ["Soltero", "Casado", "Divorciado", "Viudo"]:
    print("Estado civil inválido. Opciones: Soltero, Casado, Divorciado, Viudo.")
    estado_civil = input("Ingresa tu estado civil: ")

# Número de legajo (4 cifras, sin ceros a la izquierda)
legajo = int(input("Ingresa tu número de legajo (4 cifras, sin ceros a la izquierda): "))
while legajo < 1000 or legajo > 9999:
    print("Legajo inválido. Debe ser un número de 4 cifras, sin ceros a la izquierda.")
    legajo = int(input("Ingresa tu número de legajo: "))

# Mostrar resultados
print("\n--- Datos cargados correctamente ---")
print("Apellido:", apellido)
print("Edad:", edad)
print("Estado civil:", estado_civil)
print("Legajo:", legajo)