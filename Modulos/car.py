class Car:
    #atributos públicos
    encendido=False
    velocidad=0
    _altura=1.5
    _ancho=2.5
    _velocidadMaxima=100
     #atributos privados
    __llave="123456"
    def __init__(self,llave,color,modelo,marca):
        self.__llave=llave
        self.color=color
        self.modelo=modelo
        self.marca=marca
   
    #metodos públicos
    def encender(self,llave):
        if self.__llave==llave:
            self.encendido=True
            print("El auto",self.marca,"ya encendió")
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
            self.bocina(True)
    
    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self,valor):
        self.__matricula=valor

    @staticmethod
    def bocina(sonido=True):
        if sonido==True:
            print("Se escuchó la bocina")
        else:
            print("No se escuchó la bocina")    

    #métodos privados (sexo)
    def __enciendeLuzFreno(self):
        print("Luz del freno encendida")

