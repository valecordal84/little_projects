import random
print("Piedra Papel o Tijeras: El juego")

elementos = ["piedra", "papel", "tijeras"]

eleccion = int(input("Piedra, papel o tijera? 0 para piedra, 1 para papel, 2 para tijeras\n "))

iaEleccion = random.randint(0,2)

print(f"La ia eligió {elementos[iaEleccion]}")

if eleccion>=3 or eleccion<0:
    print("Elegiste un numero incorrecto, vuelve a intentarlo")
elif eleccion == 0 and iaEleccion == 2:
    print("Ganaste")
elif eleccion > iaEleccion:
    print ("Ganaste")
elif iaEleccion > eleccion:
    print ("Perdiste")
else:
    print ("Es un empate")