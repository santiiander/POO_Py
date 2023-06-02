class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

class Estudiante(Persona):
    def __init__(self,nombre,edad,clave,calificacion):
        Persona.__init__(self,nombre,edad)
        self.clave=clave
        self.calificacion=calificacion

class Encargado:
    def __init__(self,codigoEncargado,departamento):
        self.codigoEncargado=codigoEncargado
        self.departamento=departamento

class EstudianteEncargado(Persona,Encargado):
    def __init__(self,nombre,edad,clave,calificacion,codigoEncargado,departamento):
        Persona.__init__(self,nombre,edad)
        Encargado.__init__(self,codigoEncargado,departamento)
        self.clave=clave
        self.calificacion=calificacion       
        self.codigoEncargado=codigoEncargado
        self.departamento=departamento

Juan=Persona("Juan",22)
print(Juan.edad,"es la edad de juan")
Maria=Estudiante("Maria",23,"15f12",9)
print(Maria.clave)

wachin=EstudianteEncargado("Juancho",32,"xdl32",9,"xd123","sexual")
print(wachin.departamento,"es el departamento de wachin")
print(wachin.clave,"es la clave del mismo gil")