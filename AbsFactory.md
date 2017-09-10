Abstract Factory
===================


El problema que intenta solucionar este patrón es el
de crear diferentes familias de objetos.

El patrón Abstract Factory está aconsejado cuando
se prevé la inclusión de nuevas familias de productos,
pero puede resultar contraproducente cuando se añaden 
nuevos productos o cambian los existentes, puesto que 
afectaría a todas las familias creadas.

Cliente: La clase que llamará a la factoría adecuada 
ya que necesita crear uno de los objetos que provee la 
factoría, es decir, Cliente lo que quiere es obtener una 
instancia de alguno de los productos (ProductoA, ProductoB).

AbstractFactory: Es la definición de la interfaces de las 
factorías. Debe de proveer un método para la obtención de 
cada objeto que pueda crear. ("crearProductoA()" y 
"crearProductoB()")

Factorías Concretas: Estas son las diferentes familias de 
productos. Provee de la instancia concreta de la que se 
encarga de crear. De esta forma podemos tener una factoría 
que cree los elementos gráficos para Windows y otra que los 
cree para Linux, pudiendo poner fácilmente (creando una
nueva) otra que los cree para MacOS, por ejemplo.

Producto abstracto: Definición de las interfaces para la 
familia de productos genéricos. En el diagrama son 
"ProductoA" y "ProductoB". En un ejemplo de interfaces 
gráficas podrían ser todos los elementos: Botón, Ventana,
Cuadro de Texto, Combo... El cliente trabajará directamente 
sobre esta interfaz, que será implementada por los diferentes
productos concretos.

Producto concreto: Implementación de los diferentes productos. 
Podría ser por ejemplo "BotónWindows" y "BotónLinux". 
Como ambos implementan "Botón" el cliente no sabrá si está en 
Windows o Linux, puesto que trabajará directamente sobre la 
superclase o interfaz.

## Estructura

```
class Pizza

	abstract Pizza crearPizza() //se define un metodo abstracto en la clase pizzeria que sera implementado en cada subclase pizzeria
	
	Pizza(FactoriaIngredientes fi); //se define de este modo por cada subclase dependiendo de la zona, mas que nada por sus proveedores...
		

	Pizza crearPizza() //el creador de pizza es el que instancia la factory concreta, en este caso la de una mexicana 
	{
    		FactoríaIngredientes fi = new IngredientesMexicana();
   		Pizza pizza = new Pizza(fi); // Uso de factory en particular
		pizza.cortar();      //metodo de clase
    		pizza.empaquetar();  //metodo de clase
    		return pizza;
	}
```
## Ejemplo:
```
# Factory/Games.py
# An example of the Abstract Factory pattern.

class Obstacle:
    def action(self): pass

class Character:
    def interactWith(self, obstacle): pass

class Kitty(Character):
    def interactWith(self, obstacle):
        print("Kitty has encountered a",
        obstacle.action())

class KungFuGuy(Character):
    def interactWith(self, obstacle):
        print("KungFuGuy now battles a",
        obstacle.action())

class Puzzle(Obstacle):
    def action(self):
        print("Puzzle")

class NastyWeapon(Obstacle):
    def action(self):
        print("NastyWeapon")

# The Abstract Factory:
class GameElementFactory:
    def makeCharacter(self): pass
    def makeObstacle(self): pass

# Concrete factories:
class KittiesAndPuzzles(GameElementFactory):
    def makeCharacter(self): return Kitty()
    def makeObstacle(self): return Puzzle()

class KillAndDismember(GameElementFactory):
    def makeCharacter(self): return KungFuGuy()
    def makeObstacle(self): return NastyWeapon()

class GameEnvironment:
    def __init__(self, factory):
        self.factory = factory
        self.p = factory.makeCharacter()
        self.ob = factory.makeObstacle()
    def play(self):
        self.p.interactWith(self.ob)

g1 = GameEnvironment(KittiesAndPuzzles())
g2 = GameEnvironment(KillAndDismember())
g1.play()
g2.play()
```

