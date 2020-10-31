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
    
    edad = input("Que edad tienes? ")
    
    while validaEdad(edad)== False:
        print("Error, edad invalida. ")
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
        
edad = pedirEdad()
precioTotal = 0

while edad != 0:
    precioEntrada = calcularPrecioEntrada(edad)
    print("Precio Entrada {}".format(precioEntrada))
    precioTotal += precioEntrada
    
    edad = pedirEdad()
    
print("Precio total: {}".format(precioTotal))
        
    
