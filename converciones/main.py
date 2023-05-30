## CONVERSIONES STRING NÚMEROS
numero='10'
numeroConvertido=int(numero)
print(type(numero))
print(type(numeroConvertido))

flotanteString='10'
flotanteNumero=float(flotanteString)

print(flotanteString)
print(flotanteNumero)

numeroEntero=20
numeroString=str(numeroEntero)

print(type(numeroEntero))
print(type(numeroString))

##los programas se manejan de manera secuencial
##control de flujo
#1. Condicionales
###se realiza algo si se cumple cierta condición
###bloques
####cuando nosotros utilicemos cualquier control de flujo o funciones el código que se debe ejecutar después deberá estar definida por bloques o identaciones
edad=41
if edad<18:
	print('cana')
if edad>18:
	print ('ya con confianza')
if edad>40:
	print('necesita regeneración')


nombre='axel'
mensaje='hola bichota'
print(mensaje)
print(nombre)