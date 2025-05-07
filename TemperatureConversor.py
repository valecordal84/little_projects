unidad = input("Elija su unidad de medida Celsius o Fahrenheit (C - F): ")
temperatura = float(input("Ingrese la temperatura: "))

if unidad == "C":
	temperatura = round((9 * temperatura) / 5 + 32, 1)
	print(f" La temperatura en Fahrenheit es: {temperatura} °F")
elif unidad == "F":
	temperatura = round ((temperatura - 32) * 5/9 ,1)
	print(f" La temperatura en Celsius es: {temperatura} °C")
else:
	print(f"{unidad} no es una unidad válida para convertir")