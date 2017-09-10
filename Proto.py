#Prototype Pattern
#Especifica los tipos de objetos a crear por medio de una instancia
#prototípica, y crea nuevos objetos copiando dicho prototipo. 
#Este programa es de software libre puede reedistribuirse  y/o modificarse
#bajo los terminos de de GNU

import copy

class Prototype:

    #Object, that can be cloned.
    #This is just a base class, so the clone() method
    #is not implemented. But all subclasses have to
    #override it.
    #Objeto que puede ser clonado
    #Esta solo es una clase base, asi que el metodo clone()
    #No esta implementado. Pero todas las subclases deben de
    #anularlo
    

    _type  = None
    _value = None

    def clone(self):
        pass

    def getType(self):
        return self._type

    def getValue(self):
        return self._value

class Type1(Prototype):

    #Concrete prototype.
    
    #Implementation of Prototype. Important part is the
    #clone() method.
    #   Prototipo concreto
    #Implementacion del prototipo. La parte importante
    #es el metodo clone()
    

    def __init__(self, number):
        self._type = "Type1"
        self._value = number

    def clone(self):
        return copy.copy(self)

class Type2(Prototype):
    """ Concrete prototype. """

    def __init__(self, number):
        self._type = "Type2"
        self._value = number

    def clone(self):
        return copy.copy(self)

class ObjectFactory:

    #Manages prototypes.
    #Static factory, that encapsulates prototype
    #initialization and then allows instatiation
    #of the classes from these prototypes.
    #   Gestiona el prototipo.
    #Static factory, que encapsula la inicializacion
    #del prototipo y luego permite instancias de la
    #clase de estos prototipos.
    

    __type1Value1 = None
    __type1Value2 = None
    __type2Value1 = None
    __type2Value2 = None

    @staticmethod
    def initialize():
        ObjectFactory.__type1Value1 = Type1(1)
        ObjectFactory.__type1Value2 = Type1(2)
        ObjectFactory.__type2Value1 = Type2(1)
        ObjectFactory.__type2Value2 = Type2(2)
        
    @staticmethod
    def getType1Value1():
        return ObjectFactory.__type1Value1.clone()

    @staticmethod
    def getType1Value2():
        return ObjectFactory.__type1Value2.clone()

    @staticmethod
    def getType2Value1():
        return ObjectFactory.__type2Value1.clone()

    @staticmethod
    def getType2Value2():
        return ObjectFactory.__type2Value2.clone()


def main():
    ObjectFactory.initialize()

    instance = ObjectFactory.getType1Value1()
    print "%s: %s" % (instance.getType(), instance.getValue())

    instance = ObjectFactory.getType1Value2()
    print "%s: %s" % (instance.getType(), instance.getValue())

    instance = ObjectFactory.getType2Value1()
    print "%s: %s" % (instance.getType(), instance.getValue())

    instance = ObjectFactory.getType2Value2()
    print "%s: %s" % (instance.getType(), instance.getValue())


if __name__ == "__main__":
    main()
