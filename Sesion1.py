import math
import numpy as np #NECESARIO "pip install numpy"
#Ejercicio1 
def Ejercicio1():
    print("Ejercicio 1: ")
    a = (3*5)/(2+3)
    print(a)
    b = (math.sqrt(7+9))*2
    print(b)
    c = math.pow((4-7),2)
    print(c)
    d = 6 % 4
    print(d)

#Ejercicio2 
def Ejercicio2():
    print("Ejercicio 2: ")
    decision = 1
    while decision != 0:
        lista = [1,2,3,4,5,6]
        print("Introduce un valor de inicio")
        inic = int(input())
        print("Introduce un valor de fin")
        fin = int(input())
        print('')
        for n in range(inic,fin+1,1):
            print(n)
        print('')
        print("Introduce 0 si quieres dejar de buscar valores en la lista")
        decision = int(input())
        print('')

#Ejercicio3
def Ejercicio3():
    print("Ejercicio 3: ")
    a = list(range(10))
    b = list(range(1,10))
    c = list(range(1,10,2))
    print((a))
    print((b))
    print((c))
    print('')

#Ejercicio4
def Ejercicio4(): 
    print("Ejercicio 4: ")
    a = list(range(10))
    b = list(range(1,10))
    c = list(range(1,10,2))
    print(len(a))
    print(len(b))
    print(len(c))
    print(a+b)
    print(c*3)
    print('')

#Ejercicio5
def Ejercicio5():
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    m = np.array(mat)
    print(m)
    print('')
    print(m[1-1,2-1])
    print('')
    print(m[1-1,:])
    print('')

#Ejercicio6
def Ejercicio6():
    mat = [[4,1,5],[3,2,4],[9,0,1]]
    m = np.array(mat)
    print(m)
    print('')

#Ejercicio7
def Ejercicio7():
    mundial = {"Spain": 12, "Netherlands": 11, "Italy": 10, "Germany": 8, "France": 6, "Portugal": 5}
    print('')
    return mundial

#Ejercicio8 
def Ejercicio8():
    mundial = Ejercicio7()
    print(mundial)
    print(mundial["Spain"])
    print(mundial["Portugal"])
    print(mundial["Spain"]+3)
    print(mundial["France"]-2)
    print('')
   
#Ejercicio9 
def Ejercicio9():
    inventario = {'manzanas': 430, 'bananas': 312, 'naranjas': 525, 'peras' : 217}
    print(inventario['manzanas']+20)
    print(inventario['peras']-110)

#Ejercicio10
def Ejercicio10():
    s  = int(input("Cuantos segundos han pasado desde las 00:00?: "))
    horas = s/3600
    s%=3600
    minutos = s/60
    segundos = s%60 
    print("Han pasado: ", horas ," horas, " , minutos ," minutos, " , segundos ," segundos")
    ''' NO SE CONCATENA EN PYTHON '''

#Ejercicio11
def Ejercicio11():
    n = input("Introduce tu nombre: ")
    a = input("Introduce tu primer apellido: ")
    a2 = input("Introduce tu segundo apellido: ")
    f = int(input("Introduce el dia de tu nacimiento: "))
    f2 = input("Introduce tu mes de nacimiento: ")
    f3 = int(input("Introduce el año en el que naciste: "))
    print("Nombre: ", n)
    print("Primer Apellido: ", a)
    print("Segundo apellido: ", a2)
    print("Fecha de nacimiento: ")
    print("  Dia: ", f)
    print("  Mes: ", f2)
    print("  Año: ", f3)
    print(n,a,a2,'nació el ',f, ' de ', f2 , ' de ' , f3)

#Ejercicio12
def Ejercicio12():
    radio = int(input("Cual es el radio de la esfera: "))
    area = math.pi * pow(radio,2)
    print("El area del circulo es: ", area, " m2")

#Ejercicio13
def Ejercicio13():
    IVA = 0.18
    Objeto = int(input("Introduce el precio del producto sin IVA: "))
    ObjetoF = Objeto + Objeto * IVA
    print("El precio final es de: ", ObjetoF,"€ ")


#Ejercicio14
def Ejercicio14():
    x = int(input("Introduce el valor de x: ")) 
    polinomio = pow(x,4)+pow(x,3)+2*pow(x,2)+-x
    print("El resultado del polinomio es = ", polinomio)

#Ejercicio15 
def Ejercicio15():
    l1 = int(input("Introduce el primer lado: "))
    l2 = int(input("Introduce el segundo lado: "))
    perimetro = l1*2+l2*2
    area = l1*l2
    print("El area del rectangulo es: ", area, " y el perimetro es: ", perimetro)

    
#Llamada a ejercicios    
Ej = -1
while Ej!=0:
    Ej = int(input("Que ejercicio quieres?: "))
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
    if Ej == 10:
        Ejercicio10()
    if Ej == 11:
        Ejercicio11()
    if Ej == 12:
        Ejercicio12()
    if Ej == 13:
        Ejercicio13()
    if Ej == 14:
        Ejercicio14()
    if Ej == 15:
        Ejercicio15()
