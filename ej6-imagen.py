"""/*
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo:
 *   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
 //// No es necesario descargar la img
 TODO clasificacion según tamaño 
https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.APUPLLycqR6YuXfxkiVNsAHaEb%26pid%3DApi&f=1&ipt=e9e9039239688c3e38f8854fbba5ed04acd0d8da937ca27e51d519c8d3b400a3&ipo=images
 */"""

import requests
from PIL import Image
from io import BytesIO

img = input(f"Mete URL de imagen\n")
r = requests.get(img)
image = BytesIO(r.content)

if(r.status_code == 200):
    print("El link funciona, imagen obtenida")
else:
    print("Error de lectura")

im = Image.open(image)
print(f"Tamaño: {im.size}")
