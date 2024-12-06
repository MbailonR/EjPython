"""
Escribe un programa que muestre por consola los numeros de 1 a 100 (ambos incluidos y con un salto de linea entre cada uno) sustituyendo los siguientes:
-Multiplos de 3 por "fizz"
-Múltiplos de 5 por "buzz"
-Multiplos de 3 y de 5 por "fizzbuzz"
"""
for numero in range(0, 101): #numero no tiene que estar definido antes
    if(numero % 3 == 0 and numero % 5 == 0):
        print ("fizzbuzz")
    elif (numero % 3 == 0):
        print("fizz")
    elif (numero % 5 == 0): # //Mira el paciente
        print("buzz")    
    else:
        print(numero)
    print()
