import string # Biblioteca usada para crear un abecedario para las filas del tablero    
import re # Biblioteca usada para el uso de expresiones regulares

''' 
COSAS QUE HACER:
    - El fichero empieza a leer en la primera linea con letras
    - El juego acaba cuando el fichero se quede sin letras 
    - Arreglar Movimiento
    - Metodo para comprobar si hay algun hueco por debajo para rellenar 
    
'''

def abrirArchivo():
    # Con este metodo abrimos el archivo validando la existencia de este
    try:
        archivo = open("Pruebas.txt","r")
        return archivo
    except FileNotFoundError:
        print("No se ha encontrado el archivo")
        Valor = False

    return Valor

def dibujartablero(tablero):
    # Con este metodo dibujamos el tablero
    LineaH = '  +---+---+---+---+---+---+---+---+---+---+'
    abecedario = list(string.ascii_uppercase) #Una lista con todas las letras del abecedario en UpperCase
    print(LineaH)
    imprimir = ''
    for y in range(12):
        print(abecedario[y] +" |", end='')    #Con a[y] escogemos la letra de la lista correspondiente a la fila
        for x in range(10):                   #Dependiendo del valor que este en la posicion del tablero se imprime una celda u otra, manteniendo asi los valores de cada posicion para usarse
            if tablero[x][y] == "b0":
                imprimir = chr(36)*3 +chr(36)
            if tablero[x][y] == "b1":
                imprimir = chr(36)*3 + "|"
            if tablero[x][y] == "a0":
                imprimir = chr(35)*3 +chr(35)
            if tablero[x][y] == "a1":
                imprimir = chr(35)*3 + "|" 
            if tablero[x][y] == "space":
                imprimir = "   " + "|" 
            if tablero[x][y] == '000':
                imprimir = "   " + "|"
            print(""+(imprimir),end="")
        print("")
        print(LineaH)
    print('    0   1   2   3   4   5   6   7   8   9  ')
    
    return None

def reiniciartablero(tablero):
    # Con este metodo reiniciamos el tablero y lo dejamos en blanco 
    for x in range(10):
        for y in range(12):
            tablero[x][y] = '000'

    return None

def creartablero():
    # Creamos el tablero vacio y lo devolvemos para usarlo como parametro 
    tablero = []
    for i in range(12):
        tablero.append([' '] * 12)
 
    return tablero

def siguienteFila(tablero,archivo):
    # Leemos el archivo letra a letra y colocamos cada conjunto de # o $ en el tablero, teniendo en cuenta las que esten juntas
    x = 0
    linea = archivo.readline()
    if linea == "":
        print("Se han terminado las filas del fichero :(")
        return False
    else:
        for letra in range(len(linea)):
            caract = linea[letra]    
            if(caract == "B"):
                if(linea[letra+1] == "B"):
                    tablero[x][0] = "b0"
                else:
                    tablero[x][0] = "b1"
            if(caract == "b"):
                if(linea[letra-1] == "b"):
                    tablero[x][0] = "b0"
                else:
                    tablero[x][0] = "b1"
            if(caract == "A"):
                if(linea[letra+1] == "A"):
                    tablero[x][0] = "a0"
                else:
                    tablero[x][0] = "a1"
            if(caract == "a"):
                if(linea[letra+1] == "a"):
                    tablero[x][0] = "a0"
                else:
                    tablero[x][0] = "a1"
            if(caract == " "):
                tablero[x][0] = "space"
            x = x+1

        return True

def comprobarDebajo(tablero):
    for y in range(11):
        for x in range(10):
            if (tablero[x][y+1] == "space" or tablero[x][y+1] == "000") and  y<11:
                tablero[x][y+1] = tablero[x][y] 
                tablero[x][y] = '000'
            else:
                if (tablero[x][y+1] != "space" or tablero[x][y+1] != "000") and  y<11:
                    tablero[x][y] = tablero[x][y]

    return None

def comprobarDebajoP(tablero):
    for y in range(11):
        for x in range(10):
            if (tablero[x][y+1] == "space" or tablero[x][y+1] == "000") and  y<11:
                tablero[x][y+1] = tablero[x][y] 
                tablero[x][y] = '000'
            else:
                if (tablero[x][y+1] != "space" or tablero[x][y+1] != "000") and  y<11:
                    tablero[x][y] = tablero[x][y]


def comprobarFilaCompleta(tablero):
    Valor = 0
    fila = []
    cont = 11
    while cont >= 0:
        for x in range(10):
            fila.append(tablero[x][cont])
        if "space" in fila or "000" in fila:
            Valor = Valor
        else:
            Valor = True
            for x in range(11):
                tablero[x][cont] = "000"
                Valor = Valor + 1
                comprobarDebajoP(tablero)
        fila = []
        cont -= 1
    
        
    return Valor
    
def bajarFila(tablero):   
    # Bajamos la fila a la posicion que no esté llena y eliminamos la fila de arriba del todo 
    for x in range(10):
        if indice<=11:
            tablero[x][indice] = tablero[x][0]
            tablero [x][0] = '000'

    return None

def detectarJugada():       
    # Validacion de jugadas (Como en un antivirus -- VALIDACION POR MATCHING) 
    Jugada = ''
    while Jugada == '' or validarJugada(Jugada)==False:
        Jugada = input("Introduce una jugada: ")
    
    return Jugada

def validarJugada(Jugada):  
    # Primera Columna: [A-L] {1}, Segunda Columna: [0-9] {1}, Tercera Columna: [<, >] {1} ; Tambien es valido: [-]{3}      
    if re.match("[A-L]{1}[0-9]{1}[<,>]{1}",Jugada) and len(Jugada) == 3:
        return True
    if re.match("[-]{3}",Jugada) and len(Jugada) == 3:
            return True

    return False
    
def detectarDecision():       
    # Validacion de jugadas (Como en un antivirus -- VALIDACION POR MATCHING) 
    Decision = ''
    while Decision == '' or validarDecision(Decision)==False:
        Decision = input("Quieres Jugar? (Y/N): ")
    
    return Decision

def validarDecision(Decision):  
    # Primera Columna: [A-L] {1}, Segunda Columna: [0-9] {1}, Tercera Columna: [<, >] {1} ; Tambien es valido: [-]{3}      
    if re.match("[Y,N]{1}",Decision) and len(Decision) == 1:
        return True
    return False

def convertirAscii(tablero,Jugada):
    # Detectamos la posicion de las filas convirtiendo ASCII a un int, sin embargo, validamos si en cada posición hay un "-" para detectar el movimiento nulo  
    if Jugada[0] == "-":
        Fila = 0
    else:
        Fila = ord((Jugada[0]))-65
    if Jugada[1] == "-":
        Columna = 0
    else:
        Columna = int(Jugada[1])
    if Jugada[2] == "-":
        Movimiento = 0 
    else:
        Movimiento = 0
        if Jugada[2] == "<":
            Movimiento = -1  # Izquierda
        else: 
            Movimiento = 1   # Derecha
    Condiciones = {"F":Fila, "C": Columna, "M": Movimiento }

    return Condiciones

def realizarMovimiento(Condiciones,tablero):
    # Obtenemos los int del diccionario que hemos devuelto en el metodo convertirAscii(), y hacemos el movimiento correspondiento correspondiente siguiendo todas las normas del juego
    Columna = Condiciones["C"]
    Fila = (Condiciones["F"])
    moveraColumna = (Condiciones["C"])+(Condiciones["M"])
    if (Condiciones["C"]) !=  0:
        if tablero[moveraColumna][Fila] == '000' or tablero[moveraColumna][Fila] == "space":
            if tablero[Columna][Fila] == "b0" or tablero[Columna][Fila] == "b1":
                if tablero[Columna-1][Fila] == "b0" or tablero[Columna-1][Fila] == "b1" :
                    if tablero[Columna-2][Fila] == "b0" or tablero[Columna-2][Fila] == "b1":
                        if tablero[Columna-3][Fila] == "b0" or tablero[Columna-3][Fila] == "b1":
                            tablero[moveraColumna][Fila] = "b1"
                            tablero[Columna][Fila] = "b0"
                            tablero[Columna-1][Fila] = "b0"
                            tablero[Columna-2][Fila] = "b0"
                            tablero[Columna-3][Fila] = 'space'
                        else:
                            tablero[moveraColumna][Fila] = "b1"
                            tablero[Columna][Fila] = "b0"
                            tablero[Columna-1][Fila] = "b0"
                            tablero[Columna-2][Fila] = 'space'    
                    else:    
                        tablero[moveraColumna][Fila] = "b1"
                        tablero[Columna][Fila] = "b0"
                        tablero[Columna-1][Fila] = 'space'
                else:
                    if tablero[Columna+1][Fila] == "b0" or tablero[Columna+1][Fila] == "b1" :
                        if tablero[Columna+2][Fila] == "b0" or tablero[Columna+2][Fila] == "b1":
                            if tablero[Columna+3][Fila] == "b0" or tablero[Columna+3][Fila] == "b1":
                                tablero[moveraColumna][Fila] = "b0"
                                tablero[Columna][Fila] = "b0"
                                tablero[Columna+1][Fila] = "b0"
                                tablero[Columna+2][Fila] = "b1"
                                tablero[Columna+3][Fila] = 'space'
                            else:
                                tablero[moveraColumna][Fila] = "b0"
                                tablero[Columna][Fila] = "b0"
                                tablero[Columna+1][Fila] = "b1"
                                tablero[Columna+2][Fila] = 'space'    
                        else:    
                            tablero[moveraColumna][Fila] = "b0"
                            tablero[Columna][Fila] = "b1"
                            tablero[Columna+1][Fila] = 'space'
                    else: 
                        tablero[moveraColumna][Fila] = tablero[Columna][Fila]
                        tablero[Columna][Fila] = '000'
            if tablero[Columna][Fila] == "a0" or tablero[Columna][Fila] == "a1":
                if tablero[Columna-1][Fila] == "a0" or tablero[Columna-1][Fila] == "a1" :
                    if tablero[Columna-2][Fila] == "a0" or tablero[Columna-2][Fila] == "a1":
                        if tablero[Columna-3][Fila] == "a0" or tablero[Columna-3][Fila] == "a1":
                            tablero[moveraColumna][Fila] = "a1"
                            tablero[Columna][Fila] = "a0"
                            tablero[Columna-1][Fila] = "a0"
                            tablero[Columna-2][Fila] = "a0"
                            tablero[Columna-3][Fila] = 'space'
                        else:
                            tablero[moveraColumna][Fila] = "a1"
                            tablero[Columna][Fila] = "a0"
                            tablero[Columna-1][Fila] = "a0"
                            tablero[Columna-2][Fila] = 'space'    
                    else:    
                        tablero[moveraColumna][Fila] = "a1"
                        tablero[Columna][Fila] = "a0"
                        tablero[Columna-1][Fila] = 'space'
                else:
                    if tablero[Columna+1][Fila] == "a0" or tablero[Columna+1][Fila] == "a1" :
                        if tablero[Columna+2][Fila] == "a0" or tablero[Columna+2][Fila] == "a1":
                            if tablero[Columna+3][Fila] == "a0" or tablero[Columna+3][Fila] == "a1":
                                tablero[moveraColumna][Fila] = "a0"
                                tablero[Columna][Fila] = "a0"
                                tablero[Columna+1][Fila] = "a0"
                                tablero[Columna+2][Fila] = "a1"
                                tablero[Columna+3][Fila] = 'space'
                            else:
                                tablero[moveraColumna][Fila] = "a0"
                                tablero[Columna][Fila] = "a0"
                                tablero[Columna+1][Fila] = "a1"
                                tablero[Columna+2][Fila] = 'space'    
                        else:    
                            tablero[moveraColumna][Fila] = "a0"
                            tablero[Columna][Fila] = "a1"
                            tablero[Columna+1][Fila] = 'space'
                    else: 
                        tablero[moveraColumna][Fila] = tablero[Columna][Fila]
                        tablero[Columna][Fila] = '000'
        else: 
            realizarMovimiento(convertirAscii(tablero,detectarJugada()),tablero)        
    else:
        tablero[moveraColumna][Fila] = tablero[Columna][Fila]
        
    return None

def hasPerdido(tablero,Jugar):
        if (indice<1) :
            Jugar = False
            print()
            print("              | HAS   PERDIDO |")
            print()

            return Jugar
        else:
            Jugar = True

            return Jugar



indice = 12
Jugar = True
tablero = creartablero()
if abrirArchivo():
    archivo = abrirArchivo()
else: 
    Jugar = False
reiniciartablero(tablero)
if Jugar == True:
    if detectarDecision() == "Y":
        Jugar = True
        siguienteFila(tablero,archivo)
    else:
        Jugar = False
if Jugar == True:
    dibujartablero(tablero)
    realizarMovimiento(convertirAscii(tablero,detectarJugada()),tablero)
    comprobarDebajo(tablero)
    siguienteFila(tablero, archivo)
    indice = indice-1
while Jugar==True:
    dibujartablero(tablero)
    realizarMovimiento(convertirAscii(tablero,detectarJugada()),tablero)
    comprobarDebajoP(tablero)
    indice = indice + comprobarFilaCompleta(tablero)
    Jugar = hasPerdido(tablero,Jugar)
    if siguienteFila(tablero,archivo) == False:
        Jugar = False
    indice = indice - 1
