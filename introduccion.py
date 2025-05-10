#Aunque la programacion parece una ciencia extacta (debido a su estrcho vinculo con las matematicas), programar es hacer
#que la computadora resuelva nuestros problemas. Encontrar la solucion a un problema es un proceso creativo. El resultado
#de este proceso es un programa: una descripcion de la solucion al problema que puede ser ejecutada en una computadora.

#El objetivo principal de quienes programan es resolver problemas mediante el desarrollo de programas y soluciones
#informaticas, sea cual sea el entorno en el que se aplicaran.

#Aplicaciones vs Sistemas
#Muchas veces estas dos palabras se utilizan de forma indistinta, pero no significan lo mismo.
#- las aplicaciones son programas tipicamente destinados a ser usados por una unica persona y que resuelven una tarea simple
#y especifica.
#- los sistemas estan compuestos por muchos programas y aplicaciones interconectados, que son operados por  diferentes
#personas y pueden resolver problemas multiples y mas complejos. Se le llama sistema a aquellos softwares extensos y
#complejos, que estan destinados para ser usados de diferentes formas, por multiples personas, en diferentes momentos y
#para realizar tareas complejas y diversas. 
#Ejemplos de sistemas: sistema de reserva de pasajes, redes sociales, sistemas pago en linea, videojuegos online, etc.

#Algoritmo: secuencia de pasos ordenados que permiten resolver un problema, dichos pasos generalmente son mostrados en un
#diagrama de flujo.
#¿Cual es la funcion principal de los diagramas de flujo en la representacion de algoritmos? 
#Facilitar la comunicacion visual de los pasos de un algoritmo. Los diagramas de flujo permiten un rapido
#entendimiento del funcionamiento de un sistema a traves de la comunicacion visual de sus partes y relaciones.

#A la hora de programar, se deben respetar las reglas sintacticas del lenguaje que se este usando. Algunas de estas
#reglas sintacticas pueden ser la tabulacion, el uso de palabras reservadas, el orden de los pasos en una funcion,
#el orden correcto de las funciones predefinidas, etc.
#En Python, existe lo que se conoce como indentacion, que es la jerarquizacion del codigo mediante el uso del tabulador.
#Con el uso del tab se puede jerarquizar y dividir los bloques de nuestro codigo asi como tambien determinar que bloques
#estan dentro de otros. En Python, la indentacion tiene un significado sintactico, lo cual significa que el codigo sin
#indentar tendra errores. Es casi tan importante como introducir comentarios en el codigo.

#IDE: Entornos integrados de desarrollo. Son como editores de codigo pero con herramientas mas complejas y son utilizados
#para entorno de trabajo especificos, como ciencia de datos, desarrollo web, entre otros.

#¿Que caracteriza a los lenguajes de programacion de alto nivel?
#Su capacidad para abstraer detalles de bajo nivel y expresar algoritmos de manera cercana al lenguaje humano. A mayor nivel,
#mas cercania al lenguaje humano. A menor nivel, mas cercania con el lenguaje maquina.

#Python es un lenguaje de programacion creado a fines de los 80 y publicado por primera vez a fines de 1991. Lo desarrollo
#Guido Van Rosum y, si vien tuvo sus momentos de auge y declinacion, resurgio gracias a su uso extendido en el ambito del
#Analisis y la Ciencia de datos. 

#Algunas funciones de Python
print(abs(-123)) #devuelve el valor absoluto, es decir, positivo.
print(round(4.3)) #devuelve el redondeo del numero introducido.
print(round(6.7))
print(max(4, 10, 8)) #devuelve el numero mas grande.
print(min(7, 56, 2)) #devuelve el numero mas pequeño.

#Operadores de comparacion: devuelven un valor booleano.
bool = 10 > 9 #mayor que
print(bool) 

bool_2 = 11 >= 11 #mayor o igual a 
print(bool_2) 

bool_3 = 87 < 87 #menor que
print(bool_3) 

bool_4 = 87 <= 100 #menor o igual a
print(bool_4) 

bool_5 = 8 != 8 #distinto
print(bool_5) 

bool_6 = 9 == 9 #es igual a 
print(bool_6) 

#Strings o cadenas de caracteres
string = 'hola' == 'Hola'
print(string)
string_2 = 'todo el mundo' == 'todo el mundo'
print(string_2)

#Utilizacion del operador in para saber si un string se encuentra dentro de otro.
print('amor' in 'celos')
print('placer' in 'dolor')
print('historia' in 'prehistoria')
print('proteccion de las leyes' in 'El trabajo en sus diversas formas gozara de la proteccion de las leyes, las que aseguraran...')

#saber si un string empieza o termina con un string determinado.
print(str.startswith('Fundacion e Imperio', 'Fundacion')) #primero el string y luego el que queremos evaluar.
print(str.endswith('Bueno y si', 'y si'))
print(str.endswith('hola, ¿que tal', 'hola'))

#funcion len() para calcular la cantidad de caracteres que tiene un string. Se cuentan los espacios en blanco. Esta funcion
#tiene diversos usos, no es exclusiva de los strings.
print(len('prosopopeya'))
print(len('Buenos dias a todo el mundo'))
print(len('¿No tenes 5 minutos?'))
var = len('prosopopeya')
var2 = len('Buenos dias a todo el mundo')
print(var > var2) #guardamos el largo de un string en una variable para despues hacer una comparacion.

#Funciones con strings
print(str.strip('     ¿Por que tantos espacios?     ')) #elimina los espacios antes y despues de un string.
print(str.lower('¡BAJA EL VOLUMEN!')) #pasa a minusculas un string.
print(str.upper('¡Ahora si!')) #pasa a mayusculas un string.

#Operador logico and
print(len('hola') == len('chau') and len('blanco') == len('negro')) 
comp = 8 < 10
comp2 = 8 > 9
print(comp and comp2) #primero almaceno en variables los booleanos y despues los comparo
print(str.startswith('caracol', 'cara') and str.endswith('caracol', 'col'))

#Operador logico or
print(str.lower('HOLA') == 'hola' and str.lower('adios') == 'adios')
print(len('hola') > 5 or abs(-5) == 5)
print(str.upper('mumuki') == 'Mumuki' or 'amor' in "romance")
