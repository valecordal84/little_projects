print("Esto es una calculadora de propina")

cuenta = int(input("De cuanto es la cuenta? "))
propina = int(input("Cual es el porcentaje de propina que quiere dejar? "))
personas = int(input("Entre cuantas personas se va a dividir la cuenta? "))

total = (cuenta * (propina/100) + cuenta) / personas

print(f"Cada persona deberá pagar {total}")