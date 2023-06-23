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