##operaciones con numeros
##operaciones de comparacion
mayor=15>13 ##True
menor=12<15 ##True
igual=12==12 ##True
distinto=12!=10 ##True
com=12<13
#operadores logicos
var = False & False #si uno es falso el resultado sera falso
opera= False | True #vasta que uno sea verdadero para que el resultado se verdadero
#operdores aritmeticos
op=45/23/5*2
print(opera)

#ASIGNACION AUMENTADA
a=10
a+=10  ## a=a+10

#observacion
suma=False*20
##True = 1
##False = 0

##operaciones con STRING
##combinacion de cadenas (concatenacion)
letra="hola"+" "+"a todos"

##repetir cadenas
cadena="hola"*5

##obtener una cadena especifica
obtenerCadena="hola"
mensaje="fhosdn dwfbhisdufn fsdjnfo e"
texto='descripcion del texto:"esto es una cita"'
##python asigna a una cadena dos tipos de indices
##indice positivo que es de izquierda a derecha que enpiesa en 0
##el indice negativo de derecha a izquierda que enpieza en -1
##QUIERO IMPRIMIR LA LETRA L DE MI VARIABLE obtenerCadena

print(obtenerCadena[-3])
print(mensaje[-2])
print(texto)

##troceado de cadena

trocear='un mensaje'

print(trocear[2:])
print(trocear[3:6])
print(trocear[:-3])
# [inicio:final+1]
# [inicio:inocioNegativo]

ultimoString='texto largo'
ejemplo='123456'
len(ejemplo)##6
##cuanto es la cantidad de indices
##indice=5
##longitud=6
longitud=len(ultimoString)
print(ultimoString[longitud-1]) ##print(ultimoString[-1])

####pertenecia

pertenecia='hola' in 'hola mundo' #si en la derecha tiene algo igual a la derecha sera verdadero
#y si es diferente es falso
con='a'>'A'  ## codigo ASSCCI
print(con)