class Coche():
    #Atributos del coche:
    marca = ""
    modelo = ""
    matricula = ""
    #Constructor de la clase Coche:
    def __init__(self):
        return None
    def __init__(self,marca,modelo,matricula):
        self.marca = marca
        self.modelo = modelo 
        self.matricula = matricula 
        return None
    #Metodos del objeto Coche:
    def verAtributos(self):
        print(self.marca)
        print(self.modelo)
        print(self.matricula)
        return None
    def cambiarMatricula(self,matricula):
        self.matricula = matricula
        return None
if __name__=="__main__":
    c1 = Coche("Chevrolet","Yolo","2319823XQC")
    c2 = Coche("BMW", "Carro","123125EOA")
    c1.cambiarMatricula("Hola")
    coches = []
    coches.append(c1)
    coches.append(c2)
    coches[0].verAtributos()

