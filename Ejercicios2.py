import os 


#Ejercicios hechos en clase


def Ejerciciox():
    Persona1 = {"Edad": 12, "Nombre": "Antonio"}
    Persona2 = {"Edad": 15, "Nombre": "Felipe"}
    Personas = [Persona1,Persona2]
    print(Personas)
    print(Personas[0]["Edad"])

def Ejerciciox2():
    a = int(input("Introduce un numero A: "))
    b = int(input("Introduce otro numero B: "))
    if a == b:
        print("Los numeros son iguales")
    elif a<b:
        print("B es mayor que A")
    else:
        print("A es mayor que B")

def Ejerciciox3():
    Tupla = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
    entrada = int(input("Introduce un numero positivo para saber si esta en la lista: "))
    t = list(Tupla)
    t.append(3)
    Tupla = tuple(t)
    if entrada in Tupla:
        print("El numero está en la lista")
        print("Tu numero esta en la posicion: "+Tupla.index(entrada))
        print(Tupla)






#Ejercicios de la hoja 2  


def Ejercicio1():
    num = int(input("Introduce tu numero del DNI: "))
    resto = num % 23
    Letras = {0:"T",1:"R",2:"W",3:"A",4:"G",5:"M",6:"Y",7:"F",8:"P",9:"D",10:"X",11:"B",12:"N",13:"J",14:"Z",15:"S",16:"Q",17:"V",18:"H",19:"L",20:"C",21:"K",22:"E"}
    print("Tu letra del Dni es: " + Letras[resto])

def Ejercicio2():
    print("Bienvenidos a NIM")
    Pila = 50
    Total_de_Jugadas = 0
    while Pila>0:
        quitar = 6
        while quitar > 5:
            quitar = int(input("Siguiente jugador: Retira entre 1 a 5 piedras de la pila: "))
            
        Pila -= quitar
        Total_de_Jugadas += 1
    if(Total_de_Jugadas%2 == 1):
        print("Enhorabuena Jugador 1: Has ganado")
    else:
        print("Enhorabuena Jugador 2: Has ganado")

def Ejercicio3():
    Pila = 50
    Total_de_Jugadas = 0
    print("Bienvenidos a NIM")
    print("Hay un total de ", Pila, " piedras")
    print("Cada jugador puede coger entre 1 y 5 piedras, el que coja la ultima ganará: ")
    while Pila>0:
        quitar = 6
        while quitar > 5:
            quitar = int(input("Siguiente jugador: Retira entre 1 a 5 piedras de la pila: "))
            
        Pila -= quitar
        Total_de_Jugadas += 1
    if(Total_de_Jugadas%2 == 1):
        print("Enhorabuena Jugador 1: Has ganado")
    else:
        print("Enhorabuena Jugador 2: Has ganado")

def Ejercicio4_Func(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

def Ejercicio4():
    for n in range(2,100+1):
        if Ejercicio4_Func(n) == True:
           print(n," ", end="")
           
    print("")

def Ejercicio5():
    Cadena = str(input("Introduce una cadena: "))
    if (Cadena.upper()) == "".join(reversed(Cadena.upper())):
        print("Es Palindromo")
    else:
        print("No es palindromo")

def Ejercicio6_Media(lista):
    sum = 0
    for valor in lista:
        sum += valor
    Media = sum/len(lista)
    return Media
    
def Ejercicio6_Max(lista,num):
    alto = 0
    for i in range(0,len(lista)):
        if lista[i]>alto:
            alto = lista[i]
    return alto

def Ejercicio6_Min(lista,num):
    bajo = num+num+1
    for i in range(0,len(lista)):
        if lista[i]<bajo:
            bajo = lista[i]
    return bajo

def Ejercicio6():
    num = int(input("Introduce un numero: "))
    lista = []
    for n in range(num,num+num+1):
        lista.append(n)
    print("La media es igual a : ", Ejercicio6_Media(lista))
    print("El valor maximo de la lista es: " + str(Ejercicio6_Max(lista,num)))
    print("El valor minimo de la lista es: " + str(Ejercicio6_Min(lista,num)))
    
def Ejercicio7():
    matriz = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
    sum = 0
    for element in matriz:
        print(element)
    print()
    print("Los valores medios de las filas son: ")
    for i in range(len(matriz)):
        print(Ejercicio6_Media(matriz[i]))
    print("Los valores medios de las columnas son: ")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            sum += matriz[j][i] 
        media = sum/len(matriz[i])
        print(media)
        sum = 0

def Ejercicio8():
    lista1 = [1,2,3,10]
    lista2 = [2,3,4,10,12]
    listacomun = []
    for j in range(len(lista2)): 
        if lista2[j] in lista1:
            listacomun.append(lista2[j])
    print(listacomun)


'''
def Ejercicio9_AbrirFichero():
'''


def Ejercicio9():
    archivo = open('lectura.txt','r')
    lista = archivo.readlines() 
    lista2 = archivo.read() 
    num_palabras = 0
    numlin = 0  
    for linea in lista: 
        numlin += 1
        print(linea)
    print("Numero total de lineas: ", numlin)



#Llamada a ejercicios    


Ej = -1
while Ej!=0:
    Ej = int(input("Que ejercicio quieres?: "))
    if Ej == 100: 
        Ejerciciox()
    if Ej == 200:
        Ejerciciox2()
    if Ej == 300:
        Ejerciciox3()
    if Ej == 1:
         Ejercicio1()
    if Ej == 2:
         Ejercicio2()
    if Ej == 3:
        Ejercicio3()
    if Ej == 4:
        Ejercicio4()
    if Ej == 5:
        Ejercicio5()
    if Ej == 6:
        Ejercicio6()
    if Ej == 7:
        Ejercicio7()
    if Ej == 8:
        Ejercicio8()
    if Ej == 9:
        Ejercicio9()