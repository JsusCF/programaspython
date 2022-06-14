import os

def borrarPantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


i = 0
totalacomulado = 0
igvacumulado = 0
factura = []
numproductos = int(input("ingresar numero de productos: "))
while i < numproductos:
    codigo = input("ingresar el codigo del producto: ")
    nomproducto = input("ingresar el nombre del producto: ")
    cantidad = int(input("ingresar la cantidad que desee: "))
    precio = float(input("ingresar el precio del producto: "))
    total = cantidad + precio
    igv = round(total * 0.18, 2)
    totalacomulado = totalacomulado + total
    igvacumulado = igvacumulado + igv
    registro = "P-" + codigo + "  " + nomproducto + " " * (20 - len(nomproducto)) + str(cantidad) + " " * (
                10 - len(str(cantidad))) + str(precio) + " " * (7 - len(str(precio))) + str(igv) + " " * 4 + str(total)
    factura.append(registro)
    i += 1
borrarPantalla()
print("CODIGO", "NOMBRE DEL PRODUCTO", "CANTIDAD", "PRECIO", "  IGV", "  TOTAL")
for x in factura:
    print(x)
print("*"*50)
print("total: ", totalacomulado)
print("IGV: ", round(igvacumulado, 2))