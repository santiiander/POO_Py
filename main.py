from Modulos.car import Car

ferrari=Car("LL123","BlackMate","Testarossa","Ferrari")
ferrari.encender("LL123")
print("Encendido:",ferrari.encendido,"\n",
      "Velocidad:",ferrari.velocidad,"\n",
      "Color:",ferrari.color)   

fiat=Car("LL452","Blanco","Uno","Fiat")
fiat.encender("LL452")
print("Encendido:",fiat.encendido,"\n",
      "Velocidad:",fiat.velocidad,"\n",
      "Color:",fiat.color) 




"""ferrari.encender("123456")
ferrari.acelera() 
ferrari.frena()  
print("Encendido: ",ferrari.encendido,"Velocidad: ",ferrari.velocidad)   
"""
