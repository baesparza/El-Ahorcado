import random
import time

class __funciones__:
	def preparar_palabra():
		seleccionado = True
		espacios_palabra = 0
		nueva_palabra =[]
		menu = {1: "Elementos Quimicos.", 2: "Nombres.", 3: "Random.", 4: "Video Juegos"}
		print("Selecione una categoria:")
		for clave, opc in menu.items():
			print("{0})".format(clave), opc)
		while (seleccionado):
			try:
				opcion = int(input("<1, 2, 3, 4> "))
				if (opcion == 1):
					seleccionado = False
					archivo = open("quimica.txt")
					lista_palabras = archivo.readlines()
				if (opcion == 2):
					seleccionado = False
					archivo = open("nombres.txt")
					lista_palabras = archivo.readlines()
				if (opcion == 3):
					seleccionado = False
					archivo = open("random.txt")
					lista_palabras = archivo.readlines()
				if (opcion == 4):
					seleccionado = False
					archivo = open("videojuegos.txt")
					lista_palabras = archivo.readlines()
				if ((opcion != 1) and (opcion != 2) and (opcion != 3) and (opcion != 4)):
					print("Ingrese una opcion valida.")
			except ValueError:
				print("Ingrese el numero de la categoria.")
		n = random.randrange(len(lista_palabras))
		palabra = lista_palabras[n].strip()
		palabra = palabra.upper()
		archivo.close()
		for cont in range(len(palabra)):
			if (palabra[cont] == "Á"):
				nueva_palabra.append("A")
			elif (palabra[cont] == "É"):
				nueva_palabra.append("E")
			elif (palabra[cont] == "Í"):
				nueva_palabra.append("I")
			elif (palabra[cont] == "Ó"):
				nueva_palabra.append("O")
			elif (palabra[cont] == "Ú"):
				nueva_palabra.append("U")
			elif (palabra[cont] == "Ñ"):
				nueva_palabra.append("N")
			elif (palabra[cont] == "_"):
				nueva_palabra.append(" ")
			else:
				nueva_palabra.append(palabra[cont])
		palabra = "".join(nueva_palabra)
		return palabra

	def espacios_palabra(palabra):
		contador_espacios = 0
		for i in range(len(palabra)):
			if (palabra[i] == " "):
				contador_espacios += 1
		return contador_espacios

	def mensaje(contador, letras):
		print("Te quedan ",8 - contador," intentos")
		if (contador == 1):
			print("╔════╗ \n║      \n║       \n║       \n╚═══════")
		if (contador == 2):
			print("╔════╗ \n║    O \n║       \n║       \n╚═══════")
		if (contador == 3):
			print("╔════╗ \n║    O \n║    ┼  \n║       \n╚═══════")
		if (contador == 4):
			print("╔════╗ \n║    O \n║   ┌┼  \n║       \n╚═══════")
		if (contador == 5):
			print("╔════╗ \n║    O \n║   ┌┼┐ \n║       \n╚═══════")
		if (contador == 6):
			print("╔════╗ \n║    O \n║   ┌┼┐ \n║    ┴  \n╚═══════")
		if (contador == 7):
			print("╔════╗ \n║    O \n║   ┌┼┐ \n║   ┌┴  \n╚═══════")
		if (contador == 8):
			print("╔════╗ \n║    O \n║   ┌┼┐ \n║   ┌┴┐ \n╚═══════")
		print(letras)

	def reintentar():
		reintentar = input("Quieres volver a jugar. \n<SI-NO> ")
		reintentar = reintentar.upper()
		if (reintentar == "SI"):
			reintentar = True
		else:
			reintentar = False
		return reintentar

	def creditos(tiempo):
		print()
		print("GRACIAS POR JUGAR".center(50, "-"))
		time.sleep(tiempo)
		print(" _      _ \n│_/B/r1 _│\n")
		time.sleep(tiempo)
