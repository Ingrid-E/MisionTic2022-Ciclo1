# El Centro Comercial Unaleño desea comenzar a crear un carrito de compras. Para esto se requiere una tarea que será de gran utilidad a futuro: Leer y clasificar la información sobre un producto. 

# En esta ocasión se deberá leer el nombre de un producto, el costo unitario, el precio de venta al público y la cantidad de unidades disponibles. Dada esta lectura se debe imprimir el valor total que puede ganar el centro comercial por dicho producto.

# Entrada: Los valores de cada producto en una línea de código diferente. En el siguiente orden:

#         El nombre del producto
#         El costo unitario CU
#         El precio de venta al público PVP
#         La cantidad de unidades disponibles


# Salida: Se debe mostrar lo siguiente:

#         El texto “Producto” sin comillas acompañado del nombre del producto
#         El texto “CU:” sin comillas acompañado del costo unitario del mismo
#         El texto “PVP:” sin comillas acompañado del precio de venta al público
#         El texto “Unidades Disponibles:” acompañado de las unidades disponibles
#         El texto “Ganancia:” acompañado del cálculo de la ganancia por ese producto. 


#############################
#           Input           #
#############################

producto = input("Nombre del producto: ")
cu = int(input("CU: "))
pvp = int(input("PVP: "))
unidades_disponibles = int(input("Unidades disponibles: "))

print("Producto: " + producto)

print(f"CU: ${cu}")

print(f"PVP: ${pvp}")

print(f"Unidades Disponibles: {unidades_disponibles}")

#############################
#           Output          #
#############################


ganancia = (pvp - cu)*unidades_disponibles
print(f"Ganancia: ${ganancia}")