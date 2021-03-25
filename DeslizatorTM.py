import string #Biblioteca usada para crear un abecedario para las filas del tablero    
import re #Biblioteca usada para el uso de expresiones regulares

def abrirArchivo():
    try:
        archivo = open("Filas.txt","r")
        return archivo
    except FileNotFoundError:
        print("No se ha encontrado el archivo")

    return None

def drawBoard(board):
    #Con este metodo dibujamos el tablero
    LineaH = '  +---+---+---+---+---+---+---+---+---+---+'
    a = list(string.ascii_uppercase) #Una lista con todas las letras del abecedario en UpperCase
    print(LineaH)
    for y in range(12):
        print(a[y] +" |", end='') #Con a[y] escogemos la letra de la lista correspondiente a la fila
        for x in range(10):
            print(""+(board[x][y]),end="")

        print("")
        print(LineaH)
    print('    0   1   2   3   4   5   6   7   8   9  ')
    
    return None

def resetBoard(board):
    # Con este metodo reiniciamos el tablero y lo dejamos en blanco 
    for x in range(10):
        for y in range(12):
            board[x][y] = '   '

    return None

def getNewBoard():
    # Creamos el tablero vacio y lo devolvemos para usarlo como parametro 
    board = []
    for i in range(12):
        board.append([' '] * 12)
 
    return board

def siguienteFila(board,archivo):
    x = 0
    linea = archivo.readline()
    for letra in range(len(linea)):
        print(linea[letra])
    
    for letra in range(len(linea)):
        caract = linea[letra]    
        if(caract == "B"):
            if(linea[letra+1] == "B"):
                board[x][0] = chr(35)*3 + chr(35)
            else:
                board[x][0] = chr(35)*3 + "|"
        if(caract == "b"):
            if(linea[letra-1] == "b"):
                board[x][0] = chr(35)*3 + chr(35)
            else:
                board[x][0] = chr(35)*3 + "|"
        if(caract == "A"):
            if(linea[letra+1] == "A"):
                board[x][0] = chr(36)*3 + chr(36)
            else:
                board[x][0] = chr(36)*3 + "|"
        if(caract == "a"):
            if(linea[letra+1] == "a"):
                board[x][0] = chr(36)*3 + chr(36)
            else:
                board[x][0] = chr(36)*3 + "|"
        if(caract == " "):
            board[x][0] = "   " + "|"
        x = x+1

    return None

def bajarFila(board):   
    #Bajamos la fila a la posicion que no esté llena y eliminamos la fila de arriba del todo 
    for x in range(10):
        board[x][indice] = board[x][0]
        board [x][0] = '   '

    return None

def detectarJugada():       
    #Validacion de jugadas (Como en un antivirus -- VALIDACION POR MATCHING) 
    Jugada = ''
    while Jugada == '' or validarJugada(Jugada)==False:
        Jugada = input("Introduce una jugada: ")
    
    return None

def validarJugada(Jugada):  
    #Primera Columna: [A-L] {1}, Segunda Columna: [0-9] {1}, Tercera Columna: [<, >] {1} ; Tambien es valido: [-]{3}      
    if re.match("[A-L]{1}[0-9]{1}[<,>]{1}",Jugada) and len(Jugada) == 3:
        return True
    if re.match("[-]{3}",Jugada) and len(Jugada) == 3:
            return True
            
    return False

indice = 11
Jugar = True
board = getNewBoard()
archivo = abrirArchivo()
resetBoard(board)
while Jugar==True:
    siguienteFila(board,archivo)
    drawBoard(board)
    detectarJugada(board)
    bajarFila(board)
    indice = indice - 1 
    if indice <= 0:
        Jugar = False
        board[4][0] = " |HAS PERDIDO|"
drawBoard(board)
