class Car:
    #atributos públicos
    color="Rojo"
    modelo="2010"
    marca="Vocho"
    encendido=False
    velocidad=0
    #atributos privados
    __llave="123456"

    #metodos públicos
    def encender(self,llave):
        if self.__llave==llave:
            self.encendido=True
            print("El auto ya encendió")
        else:
            print("La llave es incorrecta")

    def acelera(self):
        if self.encendido==True:
            self.velocidad=self.velocidad+10

    def frena(self):
        if self.velocidad>0:
            self.velocidad=self.velocidad-10
            self.__enciendeLuzFreno()
    def apaga(self):
        if self.encendido==True:
            self.encendido=False
            self.velocidad=0

    #métodos privados (sexo)
    def __enciendeLuzFreno(self):
        print("Luz del freno encendida")

