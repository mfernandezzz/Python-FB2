def maximo(num, num2):
    if num > num2:
        return num
    elif num2 > num:
        return num2
    else:
        return 'Los numeros son iguales'
num = float(input('Escriba un numero: '))
num2 = float(input('Escriba otro numero: '))
print(maximo(num, num2))

def decision_con_moneda(moneda, comida1, comida2):
    if moneda == 'cara':
        return comida1
    else:
        return comida2
comida1 = str(input('Escriba una comida: '))
comida2 = str(input('Escriba otra comida: '))
print(decision_con_moneda('ceca', comida1, comida2))

#Ejercicio: para Emma un numero es de la suerte si es positivo, es menor a 100 y no es el 15. Crear una funcion que tomando
#en cuenta esto determine si un numero es de la suerte o no.
def numero_suerte(numero):
    return (numero > 0) and (numero < 100) and (numero != 15)
numero = int(input('Ingrese un numero: '))
print(numero_suerte(numero))

#Ejercicio: defini una funcion llamada escribir_cartelito que tome un titulo, un nombre, un apellido y arme un unico string.
def escribir_cartelito(titulo, nombre, apellido):
    return (f'{titulo} {nombre} {apellido}')
titulo, nombre, apellido = str(input('Introduzca la abreviacion de su titulo: ')), str(input('Escriba su nombre: ')), str(input('Escriba su apellido: '))
print(escribir_cartelito(titulo, nombre, apellido))

#Ejercicio: tomando en cuenta el ejercicio anterior, crea una funcion que imprima un cartelito corto (titulo y apellido) o
#un cartelito completo.
def escribir_cartelito_2(titulo, nombre, apellido, tamaño):
    if tamaño:
        return (f'{titulo} {nombre} {apellido}')
    else:
        return (f'{titulo} {apellido}') 
tamaño = True
titulo, nombre, apellido = str(input('Introduzca la abreviacion de su titulo: ')), str(input('Escriba su nombre: ')), str(input('Escriba su apellido: '))
print(escribir_cartelito_2(titulo, nombre, apellido, tamaño))

#Ejercicio: defini la funcion crear_cartelito_optimo que reciba un titulo, nombre, apellido e invoque escribir_cartelito
#para generar un cartelito corto o largo. Si el nombre y el apellido tienen mas de 15 caracteres, el cartel debe ser
#corto, de lo contrario, el cartel sera largo.
def cartelito_optimo(titulo, nombre, apellido):
    return escribir_cartelito_2(titulo, nombre, apellido, (len(nombre) + len(apellido) < 15))#la condicion es el booleano
titulo, nombre, apellido = str(input('Introduzca la abreviacion de su titulo: ')), str(input('Escriba su nombre: ')), str(input('Escriba su apellido: '))
print(cartelito_optimo(titulo, nombre, apellido))

#Ejercicio: defini una funcion llamada signo que devuelva 1 si el numero es positivo, 0 si el numero es 0 o -1 si el
#numero es negativo.
def signo(numero):
    if numero > 0:
        return 1
    elif numero == 0:
        return 0
    else:
        return -1
numero = int(input('Escriba un numero: '))
print(signo(numero))

#Ejercicio: crea una funcion llamada medalla_segun_puesto que le asigne la medalla correspondiente a los competidores
#dependiendo de su posicion.
def medalla_segun_puesto(posicion):
    if posicion == 1:
        return 'Oro'
    elif posicion == 2:
        return 'Plata'
    elif posicion == 3:
        return 'Bronce'
    else:
        return 'Sin medalla'
posicion = int(input('Posicion obtenida: '))
print(medalla_segun_puesto(posicion))

#Ejercicio: crear una funcion llamada valor_envido que devuelva el valor de envido de las cartas de truco. Sabemos que las
#cartas del 1 al 7 valen su numeracion, las cartas del 10 al 12 inclusive valen 0, no se juegan con 8s y 9s.
def valor_envido(num_carta):
    if num_carta >= 1 and num_carta <= 7:
        return num_carta
    elif num_carta >= 10 and num_carta <= 12:
        return 0
    else:
        return 'no se juega con ochos o nueves'
num_carta = int(input('Introduzca el numero de una carta: '))
print(valor_envido(num_carta))

#Ejercicio: crear una funcion para calcular los puntos de envido sabiendo que si las dos cartas son del mismo palo, el
#valor de envido es la suma de sus valores de envido mas 20. De lo contrario, el valor de envido es el mayor valor de
#envido entre ellas.
def puntos_envido_totales(val, carta, val2, carta2):
    if (carta == carta2):
        return valor_envido(val) + valor_envido(val2) + 20
    elif (carta != carta2):
        return max(valor_envido(val), valor_envido(val2))
    else:
        return 'No se juega con esas cartas'
val = int(input('Ingrese el valor de la carta: '))
carta = str.lower(input('Escriba el palo de la carta: '))
val2 = int(input('Ingrese el valor de la segunda carta: '))
carta2 = str.lower(input('Ingrese el palo de la segunda carta: '))
print(puntos_envido_totales(val, carta, val2, carta2))
#Este codigo funciona siempre y cuando no se introduzcan 8 o 9.

#Ejercicio: en el truco, los cantos tienen diferente valor. Truco vale 2, retruco vale 3 y vale cuatro vale 4.
#Crea una funcion que se llame valor_canto_truco que reciba el canto y devuelva su respectivo valor.
def valor_canto_truco(canto):
    if canto == 'truco':
        return 2
    elif canto == 'retruco':
        return 3
    elif canto == 'vale cuatro':
        return 4
    else:
        return 'eso no es un canto de truco'
canto = str.lower(input('Canto de truco: '))
print(valor_canto_truco(canto))
