import screen

screen.locate(1, 1)
print("Edad: ")

screen.locate(4, 1)
print("Entradas bebe:......")
screen.locate(5, 1)
print("Entradas niños:.....")
screen.locate(6,1)
print("Entradas jubilados:.")
screen.locate(7,1)
print("Entradas jubilados: ")

def validaEdad(e):
    try:
        n = int(e)
        if n >= 0:
            return True
        else:
            return False
    except:
        return False
    
def pedirEdad():
    
    screen.locate(1,1)
    edad = input("Que edad tienes? ")
    
    while validaEdad(edad)== False:
        print("Error, edad invalida. ")
        screen.locate(1,1)
        edad = input("Reintroduce la edad: ")
        
    return int(edad)

def calcularPrecioEntrada(e):
    
    if e > 0 and e <= 2:
        precio = 0
    elif e <= 12:
        precio = 14
    elif e <= 65:
        precio= 23
    else:
        precio = 18   
    return precio

screen.clear()
screen.locate(1, 1)
edad = pedirEdad()
precioTotal = 0
linea = 4
numEntradasB = 0
numEntradasN = 0
numEntradasA = 0
numEntradasJ = 0

while edad != 0:
    precioEntrada = calcularPrecioEntrada(edad)
    if precioEntrada == 0:
        linea = 4
        numEntradasB +=1
        screen.locate(linea, 1)
        print("{} entrada babys (  0€): {}€".format(numEntradasB, precioEntrada))
    if precioEntrada == 14:
        linea = 5
        numEntradasN +=1
        screen.locate(linea, 1)
        print("{} entrada niños   (0€): {}€".format(numEntradasN, precioEntrada))
    if precioEntrada == 18:
        linea = 6
        numEntradasA +=1
        screen.locate(linea, 1)
        print("{} entrada adulto   (0€): {}€".format(numEntradasA, precioEntrada))
    if precioEntrada == 23:
        linea = 7
        numEntradasJ +=1
        screen.locate(linea, 1)
        print("{} entrada jubilado (0€): {}€".format(numEntradasB, precioEntrada))
    precioTotal += precioEntrada
    linea+=1
    edad = pedirEdad()
    
screen.locate(linea, 3)    
print("Precio total:....{}".format(precioTotal))
        
    


