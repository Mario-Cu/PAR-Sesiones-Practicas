#Ejercicios hechos en clase
from os import system
def Ejerciciox():
    try:
        num = -1
        while num<0:
            num = int(input("Introduce un numero entero positivo: "))
    except ValueError:
        print("El dato introducido es un tipo erroneo (no int)")
    finally:
        print("Programa Finalizado") 

lista = [1,2,3,4,5,6,7,8,9,10]
def Ejerciciox2(lista):
    try: 
        bool = True 
        num = -1 
        while num < 1:
            num = int(input("Introduce un numero entero positivo: "))
        if num in lista:
            print("El numero está en la lista")
        else:
            print("El numero no esta en la lista")
        return None
    except ValueError:
        print("Valor invalido ( no int ) ")
        Ejerciciox2(lista)
       
    finally:
        print("Finalizar programa") 

def Ejerciciox3(lista):
    try: 
        valor = True
        num = -1
        while num<0: 
            num = int(input("Introduce un numero entero positivo: "))
        if num in lista:
            print("El valor está en la lista")
            print(valor)
            return valor
        valor == False
        lista.append(num)
        print("No estaba. Añado el valor a la lista")
        print(lista)
        return valor
    except ValueError:
        print("Valor introducido erroneo (No int) ")
    finally: 
        print("Programa Finalizado")
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [7,8,9]
def Ejerciciox4(parametro_fijo,*listas):
    print (parametro_fijo)
    for argumento in listas:
        print(argumento)
    if parametro_fijo in listas:
        print(parametro_fijo)
    return None
    

#Llamada a ejercicios    


Ej = -1
while Ej!=0:
    Ej = int(input("Que ejercicio quieres?: "))
    if Ej == 1: 
        Ejerciciox()
    if Ej == 2:
        Ejerciciox2(lista)
    if Ej == 3:
        Ejerciciox3(lista)
    if Ej == 4:
        Ejerciciox4(1,lista1,lista2,lista3)