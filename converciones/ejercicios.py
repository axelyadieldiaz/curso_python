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
##hacer un programa que pida al usuario su DNI si la
##longitud del DNI es 8 pida que su nombre y lo muestre 
##por consola si la longitud del DNI es mayor o menor que 
##a 8 que le muestre mensaje de error

dni = input("Ingrese su DNI: ")

if len(dni) == 8:
    nombre = input("Ingrese su nombre: ")
    print("Su nombre es:", nombre)
else:
    print("Error: La longitud del DNI debe ser 8.")

apellido = input("Ingrese su primer apellido: ")
## hacer un programa que pida al usuario ingresar su primer apellidos si su apellido
##tiene como ultimos caracteres las letras --ez-- mostar un mensaje que digas eres
##casi español si los caracteres finales son --es-- que digas eres casi peruano

if apellido[-2:] == "ez":
    print("Eres casi español.")
elif apellido[-2:] == "es":
    print("Eres casi peruano.")
else:
    print("No se puede determinar tu nacionalidad.")

##hacer un programa que le pida a un usuario di DNI compruebe qeu sea de 8 digitos
##si es correcto que sume el primer numero y el ultimo numero del DNI, mostar 
##por la pantalla la suma y el resultado
dni = input("ingrese su DNI")
suma = len [0]+[-1]
if len(dni) == 8:
    dni =print("suma del primer y el ultimo digito de tu DNI")
    print("la suma es")
else:
      print("error: la longitud de tu DNI debe ser 8.")
