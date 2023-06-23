## bucles
condicion=0
while condicion<11:
    print("condicion")
    condicion=condicion+1

hola=0
while hola<17:
    print("hola")
    hola=hola+1

edad=0
while edad != 20:
    edad=int(input("ingrese su edad: "))

nombre=""
while nombre != "si":
    nombre=input("ingresa tu nombre: ")

while True:
    nombre=input('como te llamas:')
    if nombre == 'si':
        break

for numero in range(1,20):
    print(numero)

vocales=['a','e','i','o','u']
for numero in range(0,5):
    print(vocales[numero])

for voca in vocales:
    print(vocales)

## crear una lista de cinco colores cada color que interes
## tendras que mostrar por consola, solo cuando encuentre el
## color rojo mostrara el mensaje de 
## color encontrado y se terminara la ejecucion

colores = ['azul','naranja','negro','rojo','blanco']
for color in colores:
    if color == "rojo":
        print("color encontrado.")
        break
    print(color)

lista=[]
print(lista)
primerdato=input('ingresa una fruta: ')
lista.append(primerdato)
print(lista)
segundodato=input('ingrese su segunda fruta: ')
lista.append(segundodato)
print(lista)

## crear un programa que me deje ingresar datos de una lista vacia
##en caso el usuario ingrese la palabra 'si'el programa dejara
##de pedir datos y me mkostrara la lista con todos los datos ingresados
lista_datos = []

while True:
    entrada = input("Ingrese un dato (o escriba 'si' para finalizar): ")

    if entrada == "si":
        break

    lista_datos.append(entrada)

print("Lista de datos ingresados:")
print(lista_datos)
