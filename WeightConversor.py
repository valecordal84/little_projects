peso = float(input("Ingrese su peso: "))
unidad = input("Kilos o Libras? (K o L): ")

if unidad == "K":
	peso = peso * 2.205
	unidad = "Libras"
	print (f"Su peso es: {round(peso,1)} {unidad}")
elif unidad == "L":
	peso = peso / 2.205
	unidad = "Kilogramos"
	print (f"Su peso es: {round(peso,1)} {unidad}")
else:
	print(f"la {unidad} no es válida")