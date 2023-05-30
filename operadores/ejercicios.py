##ejercicio
##escriba un programa que acepte el radio de un circulo
## y compute su area
#ENTRADA=5
#SALIDA=78.5
#formula area=pi*(radio**2)
radioCirculo=int(input('ingrese el radio del circulo'))
##proceso
Area=3.14 * (radioCirculo**2)
##salida de datos
print(f'el area del circulo es {Area}')

#ejercicio dos
##escriba un programa que acepte el radio de una esfera y obtenga
##volumen
##datos de ejemplo
##ENTRADA=5
##SALIDA=523.333333333334
radio=int(input('ingrese el radio'))
##proceso
Volumen=4/3*(3.14*radio**3)
##salida
print(f'el volumen de la esfera es {Volumen}')

#ejercicio tres
##escriba un programa que acepte la Base y la ALTURA de un triángulo
##y compruebe su area
##BASE=4 ALRURA=5
##SALIDA=10.0

##datos de entrada
Base=int(input('ingrese la base'))
Altura=int(input('ingrese la altura'))
##proceso
Area=(Base*Altura)/2
##salida
print(f'el area del triangulo es {Area}')
