import string # Biblioteca usada para crear un abecedario para las filas del tablero    
import re # Biblioteca usada para el uso de expresiones regulares

''' 
COSAS QUE HACER:
    - Cambiar los chr por variables y sustituir esas variables en DrawBoard (Asi podemos comprobar si las celdas estan juntas en cada linea)
    









'''

def abrirArchivo():
    # Con este metodo abrimos el archivo validando la existencia de este
    try:
        archivo = open("Filas.txt","r")
        return archivo
    except FileNotFoundError:
        print("No se ha encontrado el archivo")

    return None

def drawBoard(board):
    # Con este metodo dibujamos el tablero
    LineaH = '  +---+---+---+---+---+---+---+---+---+---+'
    abecedario = list(string.ascii_uppercase) #Una lista con todas las letras del abecedario en UpperCase
    print(LineaH)
    for y in range(12):
        print(abecedario[y] +" |", end='') #Con a[y] escogemos la letra de la lista correspondiente a la fila
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
    # Leemos el archivo letra a letra y colocamos cada conjunto de # o $ en el tablero, teniendo en cuenta las que esten juntas
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
    # Bajamos la fila a la posicion que no esté llena y eliminamos la fila de arriba del todo 
    for x in range(10):
        board[x][indice] = board[x][0]
        board [x][0] = '   '

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

def moverCasillas(board,Jugada):
    # Detectamos la posicion de las filas convirtiendo ASCII a un int 
    Fila = ord((Jugada[0]))-65
    Columna = Jugada[1]
    Movimiento = 0
    if Jugada[2] == "<":
        Movimiento = -1  # Izquierda
    else: 
        Movimiento = 1 # Derecha
    Condiciones = {"F":Fila, "C": Columna, "M": Movimiento }

    return Condiciones

def realizarMovimiento(Condiciones):
    print(Condiciones["M"])













indice = 11
Jugar = True
board = getNewBoard()
archivo = abrirArchivo()
resetBoard(board)
while Jugar==True:
    siguienteFila(board,archivo)
    drawBoard(board)
    realizarMovimiento(moverCasillas(board,detectarJugada()))
    bajarFila(board)
    indice = indice - 1 
    if indice <= 0:
        Jugar = False
        board[4][0] = " |HAS PERDIDO|"
drawBoard(board)
