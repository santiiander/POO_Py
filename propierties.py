class Autito:

    def __init__(self,matricula):
        self.__matricula=matricula
   
    def getMatricula(self):
        return self.__matricula    
    def setMatricula(self,valor):
        self.__matricula=valor
    

    #setter y getter de otra forma.

    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self,valor):
        self.__matricula=valor

    def frenarAuto(self):
        print("Se frenó el auto")
        self.bocina(True)


    @staticmethod
    def bocina(sonido=True):
        if sonido==True:
            print("Se escuchó la bocina")
        else:
            print("No se escuchó la bocina")    


Golsito=Autito("WWW15")
print(Golsito.getMatricula())
Golsito.matricula=("xd")
print(Golsito.getMatricula())
Autito.frenarAuto()