import random

palabras = ['comida', 'animal', 'deporte']
palabraOculta = random.choice(palabras)

caracteresPalabra = len(palabraOculta)
blanks = ""
for espacios in range(caracteresPalabra):
    blanks += "_"
print(blanks)

vidas = 6
juegoTerminado = False
letras_correctas=[]

while not juegoTerminado:
    intento = input("Adivina una letra de la plabra: ").lower()
    print(intento)

    display = ""

    for letra in palabraOculta:
        if letra == intento:
            display += letra
            letras_correctas.append(letra)
        elif letra in letras_correctas:
            display+=letra
        else:
            display += "_"

    print(display)
    
    if intento not in palabraOculta:
        vidas -=1
        print(f"Incorrecto! quedan {vidas} vidas restantes")
        if vidas == 0:
            juegoTerminado = True
            print("Perdiste")
            
    
    if "_" not in display:
        juegoTerminado=True
        print("ganaste!")