import re #Expresiones regulares
#Validacion de jugadas (Como en un antivirus -- VALIDACION POR MATCHING) 
def siguienteJugada():
    Jugada = ''
    while Jugada == '' or validarJugada(Jugada)==False:
        Jugada = input("Introduce una jugada: ")
def validarJugada(Jugada):  #Primera Columna: [A-L] {1}, Segunda Columna: [0-9] {1}, Tercera Columna: [<, >] {1}
    resultado = False       # Tambien es valido: [-]{3}
    if re.match("[A-L]{1}[0-9]{1}[<,>]{1}",Jugada) and len(Jugada) == 3:
        return True
    if re.match("[-]{3}",Jugada) and len(Jugada) == 3:
            return True
    return False
siguienteJugada()
