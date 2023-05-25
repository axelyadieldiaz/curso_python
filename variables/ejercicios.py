## convenciones para nombrar una variable 
#3lowerCarmelCase .- Se crea uniendo palabras en la que la primera letra siempre estará en minúsculas y las siguientes palabras tendrán su primera letra en mayúsculas.
##por ejemplo una variable que almacene el nombre de un amigo
def comprobarEstadoApi():
    pass
##UpperCarmelCase .- Es similar a lowerCamelCase, pero en este caso, la primera palabra también tendrá su primera letra en mayúsculas.
##Por ejemplo, una clase para trabajar con la API de Twitter, podríamos llamarla así:
class twitterApi:
    pass
##snake_case .- A diferencia de los casos anteriores, aquí uniremos las palabras mediante guiones y siempre en minúsculas.
##Usando el primer ejemplo para comprobar el estado de una API, lo escribiríamos así con este formato:
def comprobar_estado_api():
    pass
##SCREAMING_SNAKE_CASE .- En este caso, también uniremos las palabras con guiones, pero a diferencia del snake_case, aquí todas las letras deberán ir en mayúsculas.
##Esta convención se suele utilizar para declarar constantes:
class twitterApi:
    VERSION_API = 1
    URL_API = 'https://api.twitter.com'

## constantes y como se declara en python
##no hay constantes en python, pero si hay forma de declarar una constante y esperar a que los demas respenten. al final. la constante 
##sera una variable pero con un nombre caracteristico 
VERSION_DE_MI_PROGRAMA = "1.2.1.3"
##Algunos ejemplos de constantes que a veces uso son:

RUTA_API_SERVIDOR = "http://algun.sitio/asd"

##Ya que si un día cambio la ruta, tendré que cambiarla una vez  y listo. También la he usado para definir el correo del administrador en caso de error

CORREO_ADMIN = "correo@sitio.com"
PI = 3.14592
SEGUNDOS_HORA = 3600
ANCHURA_VENTANA = 760

print(f'{PI=}')
print(f'{SEGUNDOS_HORA=}')
print(f'{ANCHURA_VENTANA=}')