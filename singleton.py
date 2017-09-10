#es un patrón Singleton esta diseñado para limitar la creación de objetos pertenecientes a una clase.
#El objetivo de este patrón es el de garantizar que una clase solo tenga una instancia
#(o ejemplar) y proporcionar un punto de acceso global a ella.
#Esta patrón; por ejemplo, suele ser utilizado para las conexiones a bases de datos.

class Singleton(object):      #Almacenamos la definicion de la clase en memoria
    _instance= None           #Instancia     
    def __new__(self):        #Al llamar al constructor revisa si la instancia se cumple
        if not self._instance:#Si no hay un valor en la instancia, se crea y se regresa
            self._instance= super(Singleton,self).__new__(self) 
            self.b= 50        #Se le asigna un valor
        return self._instance #Se regresa el valor asignado

a= Singleton()   #Primero creamos una instancia de la clase y la almacenamos en la variable "x"
print (a.b)      #Llamamos a iprimir la variable "y" guardada anteriormente
a.b = 100        #Ahora le reasignamos el valor 
c= Singleton()   #Definimos "z" para ser igual a la clase que ya hemos creado debido a que regresaremos la instancia(SOLO UNA)
print (c.b)      #Imprimimos la modificacion
