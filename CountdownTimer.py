import time

tiempo = int(input("Ingrese el tiempo deseado en segundos: "))

for x in range(tiempo, 0, -1):
	segundos = x % 60
	minutos = int(x / 60) % 60
	horas = int(x / 3600) 
	print(f"{horas:02}:{minutos:02}:{segundos:02}")
	time.sleep(1)

print("ES LA HORA")