import screen

entradaQ = {
    
    'bebe':{
        'cantidad':(4, 15),
        'precioA':(4, 19),
        },
    'niño':{
        'cantidad':(5, 15),
        'precioA':(5, 19)
        },
    'adulto':{
        'cantidad':(6, 15),
        'precioA':(6, 19)
        },
    'jubilado':{
        'cantidad':(7, 15),
        'precioA':(7, 19)
        }
    }

preciosE = {
    
    'bebe': 0,
    'niño': 14,
    'adulto': 23,
    'jubilado': 18
    }
numEntradas = {
    'bebe':0,
    'niño':0,
    'adulto':0,
    'jubilado':0
    }
screen.Print("Edad: ", 1, 1)


def printScreen():
    screen.Print("Bebe....:    -", 4, 4)
    screen.Print("Niño....:    -", 5, 4)
    screen.Print("Adulto..:    -", 6, 4)
    screen.Print("Jubilado:    -", 7, 4)
    screen.Format(1)
    screen.Print("Total....:", 9, 8)
    screen.Format(0)
    
    
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
    
    edad = screen.Input("Que edad tienes? ", 1, 1)
    
    while validaEdad(edad)== False:
        
        screen.Format(0, 30, 43)
        screen.Print("Error. edad invalida.", 25, 1, True)
        screen.Reset()
        edad = screen.Input("Reintroduce la edad: ", 1, 1)
    screen.clearLine(25)
    return int(edad)

def tipoEntrada(e):
    
    if e > 0 and e <= 2:
        tipo = 'bebe'
    elif e <= 12:
        tipo = 'niño'
    elif e <= 65:
        tipo = 'adulto'
    else:
        tipo = 'jubilado'   
    return tipo

def main():
    screen.clear()
    printScreen()

    edad = pedirEdad()
    precioTotal = 0

    while edad != 0:
        tipoE = tipoEntrada(edad)
        precioE = preciosE[tipoE]
        numEntradas[tipoE] +=1
        
        screen.Print(numEntradas[tipoE], entradaQ[tipoE]['cantidad'][0], entradaQ[tipoE]['cantidad'][1])
        screen.Print("{:7.2f}€".format(precioE * numEntradas[tipoE]), entradaQ[tipoE]['precioA'][0], entradaQ[tipoE]['precioA'][1])
        precioTotal += precioE
        screen.Format(1)
        screen.Print("{:7.2f}€".format(precioTotal), 9, 19)
        screen.Format(0)
        
        edad = pedirEdad()
        
    screen.locate(12, 1)

main()
    



