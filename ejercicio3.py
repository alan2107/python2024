'''
ejercicio 3
Ingresar 5 numeros enteros, distinto de 0,
informar:
a. cantidad de pares e impares
b. el menor numero ingresado
c. De los pares el mayor numero ingresado.
d. suma de los positivos
productos de los negativos
'''

# Inicializamos las variables
cantidad_pares = 0
cantidad_impares = 0
menor_numero = None
mayor_par = None
suma_positivos = 0
producto_negativos = 1

# Pedimos al usuario que ingrese los números
for i in range(5):
    numero = int(input("Ingrese un número entero diferente de 0: "))
    
    # Verificamos si el número es par o impar
    if numero % 2 == 0:
        cantidad_pares += 1
        # Si es par, actualizamos el mayor par si es necesario
        if mayor_par is None or numero > mayor_par:
            mayor_par = numero
    else:
        cantidad_impares += 1
    
    # Actualizamos el menor número
    if menor_numero is None or numero < menor_numero:
        menor_numero = numero
    
    # Sumamos los números positivos y calculamos el producto de los negativos
    if numero > 0:
        suma_positivos += numero
    elif numero < 0:
        producto_negativos *= numero

# Mostramos los resultados
print("Cantidad de pares:", cantidad_pares)
print("Cantidad de impares:", cantidad_impares)
print("Menor número ingresado:", menor_numero)
print("Mayor número par ingresado:", mayor_par if mayor_par is not None else "No hay números pares")
print("Suma de los números positivos:", suma_positivos)
print("Producto de los números negativos:", producto_negativos)
    


