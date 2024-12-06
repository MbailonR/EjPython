"""
Escribe una función que reciba dos palabras (String) y retorne
 verdadero o falso (Bool) según sean o no anagramas.
 Un Anagrama consiste en formar una palabra reordenando TODAS
 las letras de otra palabra inicial.
 NO hace falta comprobar que ambas palabras existan.
 Dos palabras exactamente iguales no son anagrama.

"""

def comprobador (palabraUno, palabraDos):
    if palabraUno == palabraDos:
        return False
    return sorted(palabraUno) == sorted(palabraDos)

palabraUno= input(f"Mete una palabra\n").lower()
palabraDos= input(f"Mete otra palabra\n").lower()
if(comprobador(palabraUno, palabraDos)):
    print("Son anagramas")
else:
    print("No son anagramas")    