print("Bienvenidos al mejor cuestionario de Futbol! ")

inicio = input("Estas listo para jugar? (S/N) ")
puntuacion = 0
if inicio.upper() != "S":
	quit()

respuesta=input("Pregunta 1: ¿Cuál es el país que ha ganado más Copas del Mundo? \nA- Brasil \nB- Alemania \nC- Italia \nD- Argentina\n")
if respuesta.upper() == "A":
	print("Correcto!")
	puntuacion +=1
else:
	print("Incorrecto")

print (f"Su puntuacion actual es de {puntuacion}")

respuesta=input("Pregunta 2: ¿Qué jugador ha ganado más Balones de Oro? \nA- Michel Platini \nB- Cristiano Ronaldo \nC- Lionel Messi \nD- Johan Cruyff\n")
if respuesta.upper() == "C":
	print("Correcto!")
	puntuacion +=1
else:
	print("Incorrecto")

print (f"Su puntuacion actual es de {puntuacion}")

respuesta=input("Pregunta 3: ¿En qué año se celebró la primera Copa del Mundo? \nA- 1930 \nB- 1928 \nC- 1934 \nD- 1924\n")
if respuesta.upper() == "A":
	print("Correcto!")
	puntuacion +=1
else:
	print("Incorrecto")

print (f"Su puntuacion actual es de {puntuacion}")

respuesta=input("Pregunta 4: ¿Qué equipo ganó la UEFA Champions League en la temporada 2019-2020? \nA- Liverpool \nB- Bayern Múnich \nC- Paris Saint-Germain \nD- Real Madrid\n")
if respuesta.upper() == "B":
	print("Correcto!")
	puntuacion +=1
else:
	print("Incorrecto")

print (f"Su puntuacion actual es de {puntuacion}")

respuesta=input("Pregunta 5: ¿Cuál es el club con más títulos de La Liga española? \nA- Valencia \nB- Barcelona \nC- Atlético de Madrid \nD- Real Madrid\n")
if respuesta.upper() == "A":
	print("Correcto!")
	puntuacion +=1
else:
	print("Incorrecto")

print (f"Su puntuacion actual es de {puntuacion}")

respuesta=input("Pregunta 6: ¿Quién es el máximo goleador de la historia de la Premier League? A- Wayne Rooney B- Thierry Henry C- Alan Shearer D- Sergio Agüero\n")
if respuesta.upper() == "C":
	print("Correcto!")
	puntuacion +=1
else:
	print("Incorrecto")

print (f"Su puntuacion actual es de {puntuacion}")

respuesta=input("Pregunta 7: ¿Qué jugador es conocido como 'El Fenómeno'? \nA- Ronaldinho \nB- Ronaldo Nazário \nC- Zinedine Zidane \nD- Pelé\n")
if respuesta.upper() == "B":
	print("Correcto!")
	puntuacion +=1
else:
	print("Incorrecto")

print (f"Su puntuacion actual es de {puntuacion}")

respuesta=input("Pregunta 8: ¿Cuál es el estadio más grande de Europa? \nA- Camp Nou \nB- Santiago Bernabéu \nC- Wembley \nD- San Siro\n")
if respuesta.upper() == "A":
	print("Correcto!")
	puntuacion +=1
else:
	print("Incorrecto")

print (f"Su puntuacion actual es de {puntuacion}")

respuesta=input("Pregunta 9: ¿Qué selección ganó la Eurocopa 2016? \nA- Francia \nB- Portugal \nC- Alemania \nD- España\n")
if respuesta.upper() == "B":
	print("Correcto!")
	puntuacion +=1
else:
	print("Incorrecto")

print (f"Su puntuacion actual es de {puntuacion}")

respuesta=input("Pregunta 10: ¿Qué jugador argentino es conocido por el gol 'La mano de Dios'? \nA- Lionel Messi  \nB- Juan Román Riquelme \nC- Gabriel Batistuta \nD- Diego Maradona\n")
if respuesta.upper() == "D":
	print("Correcto!")
	puntuacion +=1
else:
	print("Incorrecto")

print (f"Su puntuacion final es de {puntuacion/10*100}%")


print("Gracias por jugar a mi cuestionario, espero te hayas divertido")
