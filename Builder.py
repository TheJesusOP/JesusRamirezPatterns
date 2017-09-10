#El patrón Builder separa la construcción de un objeto complejo de su representación para que el mismo proceso de construcción
#pueda crear diferentes representaciones.
#Este patrón es utilizado poe ejemplo en  restaurantes de comida rápida para construir las comidas de los clientes.
#Las cuales suelen consistir en un artículo principal (a), un artículo lateral(b)y una bebida(c). Tenga en cuenta que puede haber variación en el contenido de alimentos de los niños, pero el proceso de construcción es el mismo. 



import abc



class Director:
    
    #Construye un objeto usando la interfaz constructor
    

    def __init__(self):
        self._builder = None

    def construct(self, builder):
        self._builder = builder
        self._builder._build_part_a()
        self._builder._build_part_b()
        self._builder._build_part_c()


class Builder(metaclass=abc.ABCMeta):
  
    #Especifica una interfaz abstracta para crear partes del producto objeto
   

    def __init__(self):
        self.product = Product()

    @abc.abstractmethod
    def _build_part_a(self):
        pass

    @abc.abstractmethod
    def _build_part_b(self):
        pass

    @abc.abstractmethod
    def _build_part_c(self):
        pass


class ConcreteBuilder(Builder):
    
    #Construye y Ensambla las partes del producto implementando la interfaz builder.
    #Define y hace un seguimiento de la representación que crea.
    #Proporcionar una interfaz para recuperar el producto.

    def _build_part_a(self):
        pass

    def _build_part_b(self):
        pass

    def _build_part_c(self):
        pass


class Product:
  
    #Representa el objeto complejo bajo la construccion
    

    pass


def main():
    concrete_builder = ConcreteBuilder()
    director = Director()
    director.construct(concrete_builder)
    product = concrete_builder.product


if __name__ == "__main__":
    main()
