#Ejercicio: crear una funcion que determine si un numero es par o no y una funcion que determine lo contrario.
def es_par(numero):
    return numero % 2 == 0
def es_impar(numero):
    return numero % 2 != 0
def es_impar(numero):
    return not(es_par(numero))
print(es_par(8))
print(es_impar(8))

#Ejercicio: crea una funcion llamada mayor_de_edad y otra llamada menor_de_edad a partir de ella.
def mayor_de_edad(edad):
    return edad >= 18
def menor_de_edad(edad):
    return edad < 18
def menor_de_edad2(edad):
    return not(mayor_de_edad(edad))
edad = int(input('Ingrese su edad: '))
print(mayor_de_edad(edad))
print(menor_de_edad2(edad))

#Ejercicio: defini una funcion que se llame es_peripatetica que tome el area en que se desempeña una persona, su pais de
#origen y la cantidad de kilometros que camina por dia. Una persona es peripatetica cuando se desempeña en filosofia, 
#su pais de origen es Grecia y le gusta pasear (camina mas de 2 kilometros por dia).
def es_peripatetica(area, pais, kilometros):
    return (area == 'filosofia') and (pais == 'grecia') and (kilometros >= 2)
area = str.lower(input('¿En que area de estudio se desempeña?'))
pais = str.lower(input('¿Cual es su pais natal?'))
kilometros = float(input('¿Cuantos kilometros camina por dia?'))
print(es_peripatetica(area, pais, kilometros))

#Ejemplo de disyuncion or
def gano(cumplio_objetivo, cantidad_paises_conquistados):
    return cumplio_objetivo or (cantidad_paises_conquistados >= 30)
cantidad_paises_conquistados = int(input('Cantidad de paises conquistados: '))
print(gano(False, cantidad_paises_conquistados))

#Ejercicio: crear una funcion (o funciones) que determine si un banco esta abierto o esta cerrado. Se debe tomar en cuenta
#que el horario bancario es de 10 a 15, si es fin de semana y si es feriado.
def horarioBancario(horario):
    return horario >= 10 and horario <= 15
def esDiaHabil(dia):
    return not(dia == 'sabado' or dia == 'domingo')
def esFeriado(feriado):
    return not(feriado == 'si')
def estaAbierto(horario, dia, feriado):
    return (horarioBancario(horario) and esDiaHabil(dia) and esFeriado(feriado))
horario = int(input('Ingrese la hora en punto sin los minutos: '))
dia = str.lower(input('Ingrese un dia de la semana: '))
feriado = str.lower(input('¿Es un dia feriado? si/no: '))
if (estaAbierto(horario, dia, feriado)):
    print('La sucursal bancaria esta abierta.')
else:
    print('La sucursal bancaria esta cerrada.')

#Ejercicio: crea una funcion llamada tiene_contraste, que reciba como argumentos el color de la letra y el color de fondo
#de la pagina. La misma tiene contraste si el fondo es claro y la letra no o viceversa.
def es_tono_claro(color):
    return (color == 'rosado') or (color == 'amarillo') or (color == 'blanco') or (color == 'celeste') or (color == 'gris')
#El operador != determina que habra contraste, debido a que ambos colores tienen diferente tonalidades, ademas de ser diferentes.
def tiene_contraste(color_letra, color_fondo):
    return es_tono_claro(color_letra) != es_tono_claro(color_fondo)
color_letra = str.lower(input('Color de letra: '))
color_fondo = str.lower(input('Color de fondo: '))

print(tiene_contraste(color_letra, color_fondo))
#El ejercicio anterior corresponde a la disyuncion logica xor, y su operador es el ^. Si los valores booleanos son
#iguales el resultado sera False, y si son diferentes sera True.
#print(False ^ False)
#print(True ^ False)

#Precedencia: cuando una operacion matematica tiene varios operadores, las multiplicaciones y divisiones se efectuaran antes
#que las sumas y las restas. Al igual que en matematica, cuando se usan operadores logicos se evaluan en un orden
#determinado llamado precedencia.

#Ejercicio: crea la funcion para que determinar si 'Delfi' se puede concentrar o no. Para que se pueda concentrar la infusion 
#debe ser mate a 80Cº o te a exactamente 95Cº mas el booleano que determina si esta programando o no.
def se_puede_concentrar(bebida, temperatura, programando):
    return (bebida == 'mate' and temperatura == 80) or (bebida == 'te' and temperatura >= 95) and programando
bebida = str.lower(input('¿Que bebida esta tomando? '))
temperatura = int(input('¿A que temperatura? '))
programando = True
print(se_puede_concentrar(bebida, temperatura, programando))

#Ejercicio: establecer una funcion que determine si una persona puede subirse o no a una montaña rusa. Los requisitos para
#subir son: estatura minima de 1.5 metros (o 1.2 si esta acompañado) y no tener afecciones cardiacas. Por lo tanto, la funcion
#tendra tres parametros: la altura, si esta acompañado por un adulto y si tiene afecciones cardiacas.
def puedeSubirse(estatura, acompañado, afeccion):
    return ((estatura >= 1.5) or (estatura >= 1.2 and acompañado)) and not(afeccion)
estatura = float(input('Ingrese la estatura: '))
acompañado = False
afeccion = True

if puedeSubirse(estatura, acompañado, afeccion):
    print('Se puede subir.')
else:
    print('No se puede subir.')

#opcion 2
estatura = float(input('Ingrese la estatura: '))
acompañado = str.lower(input('¿La persona esta acompañada por un mayor? si/no: '))
afeccion = str.lower(input('¿La persona tiene alguna afeccion cardiaca? si/no: '))

if acompañado == 'si':
    acompañado = True
elif acompañado == 'no':
    acompañado = False
else:
    print('Dato incorrecto.')

if afeccion == 'si':
    afeccion = True
elif afeccion == 'no':
    afeccion = False
else:
    print('Dato incorrecto')

if puedeSubirse(estatura, acompañado, afeccion):
    print('Se puede subir.')
else:
    print('No se puede subir.')
