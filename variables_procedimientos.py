#Ejercicio: teniendo en cuenta el numero pi 3.14, crea una funcion que calcule el perimetro de un circulo y otra que
#calcule el area del circulo. El perimetro se calcula como dos veces por pi por el radio de un circulo,  el area se calcula
#como pi por radio por radio.
pi = 3.14159265358979
def perimetro_circulo(radio):
    return (pi * 2) * radio
radio = float(input('Ingrese el radio: '))
print(perimetro_circulo(radio))

def area_circulo(radio):
    return (pi * radio * radio)
radio = float(input('Ingrese el radio: '))
print(area_circulo(radio))

#Ejercicio: definir una funcion que se llame ascensor_sobrecargado que reciba una cantidad y devuelva un booleano
#determinando si el mismo esta sobrecargado o no.
carga_maxima_ascensor, peso_promedio = 300, 85
def ascensor_sobrecargado(cantidad):
    return not(cantidad * peso_promedio) < (carga_maxima_ascensor)
cantidad = int(input('Cantidad de personas en el ascensor: '))
print(ascensor_sobrecargado(cantidad))

#Existen dos tipos de variables, las globales y las locales. Las variables locales son aquellas que se declaran dentro de
#una funcion y/o procedimiento, por lo que podran ser utilizadas solo en ese ambito. Las variables globales en cambio pueden
#ser utilizadas en cualquier momento por cualquier funcion, procedimiento, etc.
def saludar_a(quien, horario):
  final_de_saludo = quien #ejemplo de declaracion de una variable local
  if horario < 12:
    return (f'¡Buenos días, {final_de_saludo}!')
  elif horario < 19:
    return (f'¡Buenas tardes, {final_de_saludo}!')
  else: 
    return (f'¡Buenas noches, {final_de_saludo}!')
  
quien = str.capitalize(input('Ingrese un nombre: '))
horario = int(input('Ingrese la hora del dia: '))
print(saludar_a(quien, horario))
  
#Si se quiere modificar una variable global a traves de un procedimiento, se debe anteponer la palabra reservada global
#a su nombre.
dias_sin_accidentes_con_velocirraptores = 0
def pasar_un_dia_normal(): #esto es un procedimiento
   global dias_sin_accidentes_con_velocirraptores #ejemplo de utilizacion de una variable global
   dias_sin_accidentes_con_velocirraptores += 1
print(dias_sin_accidentes_con_velocirraptores)
pasar_un_dia_normal() #cada procedimiento aumenta el valor de la variable en 1.
pasar_un_dia_normal()
pasar_un_dia_normal()
print(dias_sin_accidentes_con_velocirraptores) #la variable pasa a valer 3.

#Ejercicio: crear un procedimiento que, utilizando not, abra y cierre una mochila.
mochila_abierta = False
def abrir_mochila():
   global mochila_abierta
   mochila_abierta = not(mochila_abierta)
abrir_mochila()
print(mochila_abierta)
abrir_mochila()
print(mochila_abierta)

#Ejercicio: crea un procedimiento que apague y prenda una luz.
luz_prendida = True
def interruptor():
   global luz_prendida
   luz_prendida = not(luz_prendida)
interruptor()
print(luz_prendida)
interruptor()
print(luz_prendida)

#Ejercicio: 1)crea un procedimiento que simule cebar un mate. Con cada cebada, el termo pierde un poco de agua
#expresada en mililitros. 2)Crea otros dos procedimientos, uno llamado vaciar_termo y otro llamado llenar_termo.
#3) Defini el procedimiento cargar_termo que reciba una cantidad de agua y llene el termo en esa cantidad.
agua_del_termo, agua_del_mate = 1000, 0
def cebar_mate():
   global agua_del_termo
   global agua_del_mate
   agua_del_termo -= 30
   agua_del_mate += 30

def vaciar_termo():
   global agua_del_termo
   agua_del_termo = 0

def llenar_termo():
   global agua_del_termo
   agua_del_termo = 1000

def cargar_termo(cantidad):
    global agua_del_termo
    agua_del_termo += cantidad

def tomar_mate():
   global agua_del_mate
   agua_del_mate = 0

def pasar():
   pass #en Python no se pueden definir procedimientos vacios, por lo que se usa pass (es la representacion de no hacer nada).

print(agua_del_mate)
print(agua_del_termo)
cebar_mate()
print(agua_del_mate)
pasar()
print(agua_del_mate)
print(agua_del_termo)
tomar_mate()
print(agua_del_mate)
vaciar_termo()
print(agua_del_termo)
cargar_termo(500)
print(agua_del_termo)

volumen = 40 #variable global
def subir_volumen(decibeles): #procedimiento
   global volumen
   volumen += decibeles

def bajar_volumen(decibeles): #procedimiento
   global volumen
   volumen -= decibeles

def es_volumen_saludable(): #funcion
   return volumen <= 75 #retorna un booleano

subir_volumen(20) #se aumenta el volumen en 20 decibeles
print(es_volumen_saludable()) 
subir_volumen(20)
print(es_volumen_saludable())
bajar_volumen(10) #se baja el volumen en 10 decibeles
print(es_volumen_saludable())
