"""
Escribe un programa que diga si un numero es primo
Una vez hecho esto imprime los primos de 1 a 100
"""

def primoChecker(num):
    for i in range(2, num - 1):
        if(num % i == 0):
            return False
    return True

numero = input(f"Mete un numero para comprobar si es primo\n")
try:
    numero = int(numero)
except ValueError:
    print("No se consider un numero valido. Introduce un entero")
    exit()

if(numero == 1 or numero == 0):
    print("0 y 1 no son comprobables por convencion. Saliendo...")
    exit()

if(primoChecker(numero)):
    print("Es primo")
else:
    print("No es primo")

print("Primos de 1 a 100")
print("1 es un caso especial")
for i in range(2,100):
    if(primoChecker(i)):
        print(f"El numero {i} es primo")