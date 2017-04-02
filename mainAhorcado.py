from funciones import __funciones__ as func

print(("EL JUEGO DE LOS AHORCADOS").center(50, "-"))

#Variables
letras = []
letras_palabra = []
jugar = True
volverJugar = True
vidas = 1
usadas = []
lista_palabras = []
lista_numeros = []
seleccionado = True
MensajeAyuda = True

#Procesos
while (volverJugar):
	letras = []
	letras_palabra = []
	jugar = True
	vidas = 1
	usadas = []
	Bandera = True
	i = 0
	MensajeAyuda = True
	espacios_cont = 0
	espacioint = 0
	lista_numeros = []
	cont = 00

	palabra = func.preparar_palabra()

	espacios_cont = func.espacios_palabra(palabra)

	for i in range(len(palabra)):
		letras.append("_")
		letras_palabra.append(palabra[i])
		if (" " == palabra[i]):
			letras[i] = " "
			letras_palabra[i] = " "

	print()
	print("".center(50, "-"))
	func.mensaje(vidas, letras)
	print("La palabra tiene ", (len(letras) - espacios_cont) , " letras.")
	print()


	while (jugar):
		if (letras_palabra != letras):
			if (vidas <= 7):
				if ((MensajeAyuda) == (vidas >= 5)):
					letra = input('Si necesitas ayuda escribe "ayuda".\nIngrese una letra o la palabra. ')
				else:
					letra = input("Ingrese una letra o la palabra. ")
				letra = letra.upper()
				if (not (letra in usadas)):
					if (letra == "AYUDA"):
						MensajeAyuda = False
						bandera = True
						lista_numeros = [str(i) for i in range(len(letras)) if (letras[i] == "_")]
						for i in range(len(letras)):
							if ("_" == letras[i]):
								letras[i] = lista_numeros[cont]
								cont += 1
						print()
						print("".center(50, "-"))
						print("Ingrese el numero del espacio de la letra que necesita.")
						while (bandera):
							try:
								print(letras)
								espacioint = int(input("<Ayuda> "))
								espaciosrt = str(espacioint)
								if (espaciosrt in letras):
									bandera = False
								else:
									print("Numero fuera de rango, ingrese otro numero.")
							except ValueError:
								print("Ingrese solo el numero del espacio.")
						for k in range(len(letras)):
							if (espaciosrt == letras[k]):
								letras[k] = palabra[k]
						for j in range(len(letras)):
							if (letras[j] in lista_numeros):
								letras[j] = "_"
					elif (len(letra) == len(palabra)):
						if (letra in palabra):
							jugar = False
							print("*************HAS GANADO************* \nLa palabra correcta era",palabra)
							Bandera = False
					elif (len(letra) == 1):
						if (letra in palabra):
							for i in range(len(palabra)):
								if (letra == palabra[i]):
									letras[i] = letra
						else:
							vidas += 1
							print("La letra",letra,"es incorrecta, has perdido una vida.")
					elif ((len(letra) > 1) == (len(letra) != (len(palabra)))):
						print("Ingrese solo una letra a la vez.")
					else:
						vidas += 1
						print("Esa no es la palabra, has perdido una vida.")
					if(Bandera):
						func.mensaje(vidas, letras)
					usadas.append(letra)
				else:
					print("La letra",letra,"ya ha sido usada.")
			else:
				jugar = False
				print("Te has quedado sin intentos.\nLa palabra correcta era",palabra)
		else:
			print("**********HAS GANADO********** \nLa palabra correcta era",palabra)
			jugar = False
		print()
	volverJugar = func.reintentar()
	print()
func.creditos(1)
