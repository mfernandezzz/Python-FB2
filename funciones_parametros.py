#Llamar a una funcion en programacion implica ejecutar el bloque de codigo de la funcion y realizar la tarea especifica
#que esta en ella. 
#Parametro: es un valor que se espera como entrada a una funcion cuando se la declara. Es una variable que se utiliza en la
#definicion de la funcion para referirse a los datos que se pasan a la funcion cuando se la llama.

#¿Cual es la relacion entre la funcion principal y la funcion anidada en terminos de flujo de ejecucion?
#El flujo cambia a la funcion anidada y luego cambia a la funcion principal. Al finalizar la ejecucion de una funcion el
#flujo retorna al punto siguiente al que fue llamada, sea esto dentro de otra funcion, o no.

#¿En que se diferencia un procedimiento de una funcion? Los procedimientos no tienen un retorno, pero si tienen un
#efecto al ser invocados.

print(len('bombo') == len('guitarra'))
print(len('timbal') == len('flauta'))
print(len('bahia de samborombon') > len('sierra grande'))
print(len('tierra del fuego') > len('santiago del estero'))

#saber si un string es una pregunta o no, si la pregunta es en español, empieza y termina con un signo de interrogacion.
def es_pregunta(oracion):
    return str.startswith(oracion, '¿') and str.endswith(oracion, '?')
oracion = input('Escriba una oracion (puede ser una pregunta): ')
print(es_pregunta(oracion))

def mitad(numero):
    return numero / 2
numero = float(input('Ingrese un numero: '))
print(mitad(numero))

def suma_longitudes(string, string2):
    return (f'La suma de los caracteres de ambas palabras es: {(len(string)) + (len(string2))}')
string = input('Escriba un string: ')
string2 = input('Escriba otro string: ')
print(suma_longitudes(string, string2))

def son_las_doce(hora):
    return hora == 12
la_hora = int(input('Ingrese una hora: '))
print(son_las_doce(la_hora))

#Invocar funciones dentro de otra funcion, o una funcion dentro de una definicion
def doble(numero): #creamos la funcion que devuelve el doble de un numero ingresado como parametro
    return numero * 2
def siguiente_del_doble(numero): #creamos la funcion que tome la funcion anterior y le sume 1
    return doble(numero) + 1
numero = float(input('Ingrese un numero: '))
print(siguiente_del_doble(numero))
#opcion 2
def doble(numero2):
    return numero2 * 2
def siguiente(numero2):
    return numero2 + 1
def siguiente_del_doble2(numero2):
    return siguiente(doble(numero2))
numero2 = float(input('Ingrese un numero: '))
print(siguiente_del_doble2(numero2))

#Ejercicio: define una funcion anterior (que recibe un numero y devuelve uno menos), triple (el triple de un numero) y
#anterior del triple que recibe el numero triplicado y le resta 1
def anterior(entero):
    return entero - 1

def triple(entero):
    return entero * 3

def anterior_del_triple(entero):
    return anterior(triple(entero))
entero = int(input('Ingrese un numero entero: '))
print(anterior_del_triple(entero))

#Ejercicio: crear una funcion que reciba tres numeros como parametros y devuelva un booleano determinando si el primer numero es
#mayor o igual al segundo y menor o igual al tercer. Luego crear otra funcion que haga lo contrario a la primera.
def estaEntre(num, num2, num3):
    return (num >= num2) and (num <= num3)
def estaFueraRango(num, num2, num3):
    return (num <= num2) and (num >= num3)
num = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese un segundo numero: '))
num3 = int(input('Ingrese un tercer numero: '))
print(estaEntre(num, num2, num3))
print(estaFueraRango(num, num2, num3))

#Determinar si una cadena de caracteres esta incluida en una palabra.
def incluir(string):
    return palabra in string
palabra = input('Escriba una palabra: ')
string = input('Escriba otra palabra: ')
print(incluir(string))

#Ejercicio: crea una funcion que reciba un string y lo devuelva en mayusculas y entre signos de exclamacion.
def mayusculas(string):
    return (f'¡{str.upper(string)}!')
string = str(input('Escriba una palabra o palabras: '))
print(mayusculas(string))

#Ejercicio: escribi una funcion que tome un dia de semana y devuela un booleano dependiendo de si es fin de semana o no.
def es_fin_de_semana(dia):
    return dia == 'sabado' or dia == 'domingo'
dia = str.lower(input('Escriba un dia de semana: '))
print(es_fin_de_semana(dia))
