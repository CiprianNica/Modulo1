import screen

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

while edad != 0:
    precioEntrada = calcularPrecioEntrada(edad)
    screen.locate(linea, 1)
    print("Precio Entrada.....{}".format(precioEntrada))
    precioTotal += precioEntrada
    linea+=1
    edad = pedirEdad()
    
screen.locate(linea, 3)    
print("Precio total:....{}".format(precioTotal))
        
    

