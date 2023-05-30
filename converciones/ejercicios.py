##ejercicio
#haga un programa que pida al usuario y luego su
#apellido y como salida te conecte ambos

##nombre=yadiel
##apelldo=diaz

#salida "yadiel, diaz"
nombre=input("ingrese su nombre: ")
apellido=input("ingrese su apellido: ")

print (f"""
=================
"{nombre}", "{apellido}"
=================
""")


#hacer un programa que pida a un usuario un texto y me de
#como salida la cantidad de letras que tiene
##entrada=hola
##salida=4

texto=input('ingrasa un texto')
cantidadLetras=len(texto)
print(cantidadLetras)

##ejercicio
#evaluar si es menor a 17 mostrá como mensaje cana si es mayor 
#a 18 mostrar la come y si es mayor a 40 mostrar ya esta usado

edad=15
if edad<18:
	print('cana')
	if edad<40:
		print('ya come')
else:
	print('ya esta usado')