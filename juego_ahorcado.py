import random
import os

def run():
## las image fueron las busqué como hangmanwordbank.py de chrishorton    
    IMAGES  = [ '''
  + --- +
  | |
      |
      |
      |
      |
========= ''' ,'''
  + --- +
  | |
  O |
      |
      |
      |
========= ''' , '''
  + --- +
  | |
  O |
  | |
      |
      |
========= ''' , '''
  + --- +
  | |
  O |
/ | |
      |
      |
========= ''' , '''
  + --- +
  | |
  O |
 / | \ |
      |
      |
========= ''' , '''
  + --- +
  | |
  O |
 / | \ |
 / |
      |
========= ''' , '''
  + --- +
  | |
  O |
 / | \ |
 / \ |
      |
========= ''' ]
    
    DB=[
        "ACUTANGULO",
        "RECTANGULO",
        "OBTUSANGULO",
        "EQUILATERO",
        "ESCALENO",
        "ISOSCELES"
    ] ##base de las palabras que voy a usar para el juego

    word = random.choice(DB)   ##estas serán las palabras que se elegirán aleatoriamente con el random
    spaces = ["_"]*len(word)  ##los espacios_guiones que mostrará segun la cantidad de letras que tenga la palabra
    attemps = 6    ## la cantidad de intentos que pueden probar 

    while True:
        os.system("cls")
        for character in spaces:
            print(character, end=" ")
        print(IMAGES[attemps])        ##se imprime la cantidad de espacios_guiones y la imagen completa del muñeco

        letras = input ("Elige una letra ").upper() ##convierte a mayusculas con .upper() lo que ingrese el usuario, xq la base de palabras está en mayúsculas

        found = False
        for idx, character in enumerate(word):      ##recorre indices y caracteres 
            if character == letras:      ##si el espacio es igual a la letra del usuario
                spaces[idx] = letras     ## en en espacio se reemplazara por la letra
                found = True
        if not found:  ##si la letra introducida no es la correcta
            attemps -= 1   ##va restando los intentos del ciclo
        
        if "_" not in spaces:    ##si no hay hay espacio vacios, ganaste
            os.system("cls")
            print("GANASTE!")
            break ##rompe el ciclo
            input() ## se imprime cada paso

        if attemps == 0:  ## si realizaste 6 instentos y fallaste en todos perdiste
            os.system("cls")   ##limpia la pantalla en Windows
            print("PERDISTE!")
            break  ##rompe el ciclo
            input()

if __name__ =='__main__':
    run()