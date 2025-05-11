#Desafio integrador
#Consigna: crear un sencillo sistema para ser utilizado por los funcionarios que operan la caja de un comercio (el sistema
#no necesita interfaz grafica, sera manejado desde la consola). 
#Requerimientos:
#-Al iniciar, el sistema solicitara al usuario, que sera el funcionario que opera la caja registradora, que ingrese los datos
#de la compra, uno a uno: nombre del producto, cantidad adquirida, precio unitario del producto (en dolares), categoria del
#cliente (si es cliente premium o no).
#-El sistema debe luego realizar los calculos necesarios para determinar el total que el cliente debe abonar, teniendo en
#cuenta el siguiente criterio: A las compras de al menos 200 dolares (100 dolares para clientes premium) se les descontara
#un 15%. Ademas, en compras menores a 100 dolares realizadas por clientes premium, se les descontara un 5%.
#-Por ultimo, el sistema debera imprimir en pantalla la factura, con los siguientes datos: nombre del producto, cantidad
#adquirida, precio unitario del producto (en dolares), subtotal (el costo total antes de los descuentos), descuentos
#(en dolares) y total a pagar en dolares.

#Funcion para determinar los montos a pagar dependiendo el tipo de cliente y el gasto.
def datos_compra(cantidad, precio, Premium):
    if ((cantidad * precio) >= 100 and Premium) or ((cantidad * precio) >= 200 and not(Premium)):#si el cliente es premium y gasta 100 dolares o mas, o si el cliente no es premium y gasta 200 dolares o mas 
        return (cantidad * precio) - (cantidad * precio) * 15 / 100 #se le descuenta 15%
    elif (cantidad * precio) < 100 and Premium:#si el cliente es premium y gasta menos de 100 dolares
        return (cantidad * precio) - ((cantidad * precio) * 5 / 100)#al cliente premium se le descuenta 5%
    else:
        return (cantidad * precio)#si el cliente es normal y gasta menos de 200 dolares, paga sin descuento

#Funcion para imprimir la factura. 
def factura(producto, cantidad, precio, Premium):
    print('*****Factura *****')
    print(f'Nombre del producto: {producto}')
    print(f'Cantidad: {cantidad}')
    print(f'Precio por unidad: {precio}')
    print(f'Subtotal: U$S {(cantidad * precio)}')
    if (Premium and ((cantidad * precio) >= 100)) or (not(Premium) and (cantidad * precio) >= 200):
        print('Descuento del 15%')
    elif Premium and ((cantidad * precio) < 100):
        print('Descuento del 5%')
    else:
        print('Descuento del 0%')
    print(f'Redondeo: {(round(datos_compra(cantidad, precio, Premium)) - datos_compra(cantidad, precio, Premium))}')
    return (f'Total a pagar: U$S{(round(datos_compra(cantidad, precio, Premium)))}')
    
producto = str(input('Nombre del producto: '))
cantidad = int(input('Cantidad de productos: '))
precio = float(input('Precio del producto: '))
Premium = False
if str.lower(input('¿Es usted cliente premium si o no?: ')) == 'si':
    Premium = True

print(factura(producto, cantidad, precio, Premium))
